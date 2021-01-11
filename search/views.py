from django.shortcuts import render
from music.models import Album, Song

# Create your views here.

def search_album(request):
	method_dict = request.GET
	query = method_dict.get('q')
	all_songs = Song.objects.search(query)
	context = {
		'all_songs':all_songs,
		'query': query
	}
	template = 'snippets/searched_songs.html'
	return render(request,template,context)

