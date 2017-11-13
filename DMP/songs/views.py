from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView
from  .models import Song
import random

# Create your views here.
# Function based view

def songs_list_view(request):
	template_name='songs/songs_list.html'
	queryset = Song.objects.all()
	context = {
		"object_list" : queryset
	}
	return render(request, template_name, context)
	
class SongListView(ListView):
	template_name='songs/songs_list.html'
	def get_queryset(self):
		slug=self.kwargs.get('slug')
		if slug:
			queryset = Song.objects.filter(Genre__icontains=slug)
		else:
			queryset = Song.objects.all()
		return queryset

class GenreListView(ListView):
	template_name='songs/genres_list.html'
	def get_queryset(self):
		slug=self.kwargs.get('slug')
		if slug:
			queryset = Song.objects.filter(Genre__icontains=slug)
		else:
			queryset = Song.objects.all()
		return queryset
	
class SongDetailView(DetailView):
	queryset = Song.objects.all()	
#	def get_object(self,*args,**kwargs):
#		song_id = self.kwargs.get('song_id')
#		obj = get_object_or_404(Song,id=song_id)
#		return obj
