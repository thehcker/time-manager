from django.urls import path
from music import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    #path('<int:album_id>/favorite/', views.favorite, name='favorite'),
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
    url(r'^(?P<pk>[0-9]+)/update_song/<pk>/$', views.update_song, name='update_song'),
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='update-album'),
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='delete-album'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    path('all-songs/', views.all_songs, name='all_songs'),
    # url(r'^(?P<pk>[0-9]+)/create_song/$', views.CreateSongView.as_view(), name='create_song'),
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),

]
