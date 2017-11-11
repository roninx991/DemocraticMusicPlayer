from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView,ListView
from  .models import Song
import random

# Create your views here.
# Function based view

def songs_list_view(request):
	template_name='songs_list.html'
	queryset = Song.objects.all()
	context = {
		"object_list" : queryset
	}
	return render(request, template_name, context)
	
class SongListView(ListView):
	queryset = Song.objects.all()
	template_name='songs_list.html'
	
class PopListView(ListView):
	queryset = Song.objects.filter(Genre__iexact='Pop Rock')
	template_name='songs_list.html'
	
class ContemporaryListView(ListView):
	queryset = Song.objects.filter(Genre__iexact='Contemporary R&B')
	template_name='songs_list.html'
