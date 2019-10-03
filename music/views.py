# from django.shortcuts import render, get_object_or_404
# from music.models import Album, Song

# # Create your views here.
# # '/music/'
# def home(request):
# 	all_albums = Album.objects.all()
# 	context = {'all_albums': all_albums}
# 	template = 'index.html'
# 	return render(request, template,context)

		

from django.views.generic import ListView, DetailView
from music.models import Album,Song
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from music.forms import SongForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from decorators import user_required



AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

# '/music/<album_id>/'
def detail(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'detail.html', {'album': album})

def favorite(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    try:
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()
    except (KeyError, Song.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})

def favorite_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        if album.is_favorite:
            album.is_favorite = False
        else:
            album.is_favorite = True
        album.save()
    except (KeyError, Album.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


class IndexView(LoginRequiredMixin, ListView):
	login_url = '/accounts/login/'
	template_name = 'index.html'
	context_object_name = 'all_albums'

	def get_queryset(self):
		return Album.objects.all()

class DetailView(DetailView):
	model = Album
	template_name = 'detail.html'

class AlbumCreate(CreateView):
	model = Album
	fields = ['artist', 'album_title', 'genre','album_logo']
	template_name = 'album_form.html'
	success_url = reverse_lazy('index')

class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist', 'album_title', 'genre','album_logo']
	template_name = 'album_form.html'
	success_url = reverse_lazy('index')

# def album_update(request):
#     album_id = request.POST.get('album_id')
#     if album_id is not None:
#         try:
#             album_obj = Album.objects.get(id=album_id)
#         except Album.DoesNotExist:
#             return redirect("index")
#         album_obj, new_obj = Album.objects.new_or_get(request)
#         if album_obj in album_obj.album.all():
#             album_obj.model.remove(album_obj)
#         else:
#             album_obj.model.add(album_obj)  # cart_obj.products.add(product_id)
#         request.session['album_items'] = album_obj.model.count()   
# #cart_obj.products.add(product_obj)
# #return redirect(product_obj.get_absolute_url())
#         return redirect("index")

class SongUpdate(UpdateView):
    model = Song
    fields = '__all__'
    template_name = 'create_song.html'
    success_url = reverse_lazy('detail')


@login_required
@user_required
def update_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SongForm(instance=song)
    return render(request, 'update_song.html', {
        'form': form
    })

    # form = SongForm(request.POST or None, request.FILES or None)
    # album = get_object_or_404(Album, pk=album_id)
    # if form.is_valid():
    #     albums_songs = album.song_set.all()
    #     for s in albums_songs:
    #         if s.song_title == form.cleaned_data.get("song_title"):
    #             context = {
    #                 'album': album,
    #                 'form': form,
    #                 'error_message': 'You already added that song',
    #             }
    #             return render(request, 'create_song.html', context)
    #     song = form.save(commit=False)
    #     song.album = album
    #     song.save()
    #     context = {
    #         'album': album,
    #         'form': form,
    #     }        
    #     return render(request, 'detail.html', context)
    # context = {
    #         'album': album,
    #         'form': form,
    #     }


    # return render(request, 'create_song.html', context)

def songs(request, filter_by):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        try:
            song_ids = []
            for album in Album.objects.filter(pk=request.user.id):
                for song in album.song_set.all():
                    song_ids.append(song.pk)
            users_songs = Song.objects.filter(pk__in=song_ids)
            if filter_by == 'favorites':
                users_songs = users_songs.filter(is_favorite=True)
        except Album.DoesNotExist:
            users_songs = []
        return render(request, 'songs.html', {
            'song_list': users_songs,
            'filter_by': filter_by,
        })
	

def all_songs(request):
    all_songs = Song.objects.all()
    context = {'all_songs': all_songs}
    template = 'all_songs.html'
    return render(request,template, context)

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('index')

# class SongCreate(CreateView):
# 	model = Song
# 	fields = ['song_title', 'file_type', 'is_favorite']
# 	template_name = 'create_song.html'
# 	success_url = reverse_lazy('detail')

@login_required
@user_required
def create_song(request, album_id):
    form = SongForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    if form.is_valid():
        albums_songs = album.song_set.all()
        for s in albums_songs:
            if s.song_title == form.cleaned_data.get("song_title"):
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'create_song.html', context)
        song = form.save(commit=False)
        song.album = album
        song.save()
        context = {
            'album': album,
            'form': form,
        }
        # song.audio_file = request.POST['audio_file']
        # file_type = song.audio_file.split('.')[-1]
        # file_type = file_type.lower()
        # if file_type not in AUDIO_FILE_TYPES:
        #     context = {
        #         'album': album,
        #         'form': form,
        #         'error_message': 'Audio file must be WAV, MP3, or OGG',
        #     }
        #     return render(request, 'create_song.html', context)

        # song.save()
        # return render(request, 'detail.html', {'album': album})
        
        return render(request, 'detail.html', context)
    context = {
            'album': album,
            'form': form,
        }


    return render(request, 'create_song.html', context)

# class SongDelete(DeleteView):
# 	model = Song
# 	success_url = reverse_lazy('detail')
@login_required
@user_required
def delete_song(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request, 'detail.html', {'album': album})



