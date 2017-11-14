from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView
from .forms import SongCreateForm
from  .models import Song
import random
from songs.utils import unique_slug_generator
# Create your views here.
# Function based view

def song_createview(request):
	template_name='songs/form.html'
	form = SongCreateForm(request.POST or None)
	errors = None
	#queryset = Song.objects.all()
#	if request.method == "GET":
#		print(request.GET)
	#print(request.POST)
#	if request.method == "POST":
#		print(request.POST)
#		name = request.POST.get("Name")
#		singer = request.POST.get("Singer")
#		genre = request.POST.get("Genre")
#		form = SongCreateForm(request.POST)
	if form.is_valid():
		obj = Song.objects.create(
			Name = form.cleaned_data.get('Name'),
			Singer = form.cleaned_data.get('Singer'),
			Genre = form.cleaned_data.get('Genre')
		)
		obj.slug = unique_slug_generator(obj)
		obj.save()
		return HttpResponseRedirect("/songs/")
	if form.errors:
		print(form.errors)
		errors = form.errors
	template_name='songs/form.html'
	#queryset = Song.objects.all()
	context = {"form":form}
	return render(request, template_name, context)


#def songs_list_view(request):
#	template_name='songs/songs_list.html'
#	queryset = Song.objects.all()
#	context = {
#		"object_list" : queryset
#	}
#	return render(request, template_name, context)
	
class SongListView(ListView):
	template_name='songs/songs_list.html'
	def get_queryset(self):
		slug=self.kwargs.get('slug')
		if slug:
			queryset = Song.objects.filter(Genre__icontains=slug).order_by('Votes','Name')
		else:
			queryset = Song.objects.all().order_by('Votes','Name')
		return queryset

class GenreListView(ListView):
	template_name='songs/genres_list.html'
	def get_queryset(self):
		slug=self.kwargs.get('slug')
		if slug:
			queryset = Song.objects.filter(Genre__icontains=slug)
		else:
			qs = []
			g = []
			queryset = Song.objects.all().order_by('Genre')
			for item in queryset:
				if item.Genre not in g:
					g.append(item.Genre)
					qs.append(item)
			queryset = qs
			print(qs)
		return queryset
	
class SongDetailView(DetailView):
	queryset = Song.objects.all()	
#	def get_object(self,*args,**kwargs):
#		song_id = self.kwargs.get('song_id')
#		obj = get_object_or_404(Song,id=song_id)
#		return obj
