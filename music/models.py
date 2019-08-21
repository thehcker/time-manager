import random
import os
from django.conf import settings
# from accounts.models import User
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save


User = settings.AUTH_USER_MODEL


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "music/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )

# Create your models here.

class AlbumManager(models.Manager):
	def new_or_get(self,request):
		album_id = request.session.get("album_id",None)
		qs = self.get_queryset().filter(id=album_id)
		if qs.count() == 1:
			new_obj = False
			album_obj = qs.first()
			if request.user.is_authenticated and album_obj.user is None:
				album_obj.user = request.user
				album_obj.save()
		else:
			album_obj = Cart.objects.new(user=request.user)
			new_obj = True
			request.session['album_id'] = album_obj.id
		return album_obj, new_obj



class Album(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
	artist = models.CharField(max_length=100)
	album_title = models.CharField(max_length=100)
	genre = models.CharField(max_length=50)
	album_logo = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	is_favorite = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = AlbumManager()

	def get_absolute_url(self):
		return reverse('music:detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.album_title + '-' + self.artist

def pre_save_album_receiver(sender,instance,*args,**kwargs):
	album,new = Album.objects.get_or_create(user=instance)

pre_save.connect(pre_save_album_receiver, sender=User)



class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	audio_file = models.CharField(max_length=100)
	song_title = models.CharField(max_length=100)
	is_favorite = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse('music:create_song', kwargs={'pk':self.pk})

	def __str__(self):
		return self.song_title

def create_song(sender,instance,**kwargs):
	song,new = Song.objects.get_or_create(album=instance)
 
pre_save.connect(create_song,sender=Album)



class ProfileManager(models.Manager):
	def new_or_get(self,request):
		profile_id = request.session.get("profile_id",None)
		qs = self.get_queryset().filter(id=profile_id)
		if qs.count() == 1:
			new_obj = False
			profile_obj = qs.first()
			if request.user.is_authenticated and profile_obj.user is None:
				profile_obj.user = request.user
				profile_obj.save()
		else:
			profile_obj = request.user
			
		return profile_obj


class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True,related_name="profile")
	name = models.CharField(max_length=100,blank=True)
	address = models.CharField(max_length=150, blank=True)
	city = models.CharField(max_length=120,default='')
	phone = models.IntegerField(default=0)
	last_seen = models.DateTimeField(auto_now_add=True)
	description = models.TextField(max_length=150, blank=True, default="Enter your Products description")
	image = models.ImageField(upload_to='documents/',null=True)

	objects = ProfileManager()

	def __str__(self):
		return self.user.username

def create_album(sender,instance,**kwargs):
	album,new = Album.objects.get_or_create(user=instance)
 
post_save.connect(create_album,sender=User)