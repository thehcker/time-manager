from django.contrib import admin
from music.models import Album,Song

# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
	class Meta:
		model = Album

admin.site.register(Album, AlbumAdmin)
admin.site.register(Song)
