from django.urls import path
from music import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    # path('', views.home, name='index'),
    # path('<int:album_id>/', views.detail, name='detail'),
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    #path('<int:album_id>/favorite/', views.favorite, name='favorite'),
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
    path('album/<int:pk>/<song_id>', views.SongUpdate.as_view(), name='update_song'),
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='update-album'),
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='delete-album'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    # path('songs/<int:pk>/', views.songs, name='songs'),
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    # path('<int:album_id>/create_song/', views.SongCreate.as_view(), name='create_song'),
    # path('<int:pk>/delete_song/song_id/', views.SongDelete.as_view(), name='delete_song'),
     # url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.SongDelete.as_view(), name='delete_song'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
]
