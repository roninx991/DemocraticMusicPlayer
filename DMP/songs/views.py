from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from .forms import RegisterForm
from  .models import Song
from songs.utils import unique_slug_generator
# Create your views here.
# Function based view

def signup(request):
	queryset = Song.objects.all().order_by('Name')
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			for s in queryset:
				vote = form.cleaned_data.get(str(s.slug))
				if vote:
					obj = get_object_or_404(Song,id=s.id)
					obj.Votes = obj.Votes + 1
					obj.save()

		login(request, user)
		return redirect('/songs/')
	else:
		form = UserCreationForm()
	return render(request, 'home.html', {'form': form,'songs':queryset})

@login_required()
def song_createview(request):
	template_name='songs/form.html'
	form = SongDetailCreateForm(request.POST or None)
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
		if request.user.is_authenticated():
			instance = form.save(commit=False)
			
			instance.owner = request.user
			instance.save()
	#		form.save()
	#		obj = Song.objects.create(
	#			Name = form.cleaned_data.get('Name'),
	#			Singer = form.cleaned_data.get('Singer'),
	#			Genre = form.cleaned_data.get('Genre')
	#		)
	#		obj.slug = unique_slug_generator(obj)
	#		obj.save()
			return HttpResponseRedirect("/songs/")
		else:
			return HttpResponseRedirect("/login/")
	if form.errors:
		errors = form.errors
	template_name='songs/form.html'
	#queryset = Song.objects.all()
	context = {"form":form,"errors":errors}
	return render(request, template_name, context)


#def songs_list_view(request):
#	template_name='songs/songs_list.html'
#	queryset = Song.objects.all()
#	context = {
#		"object_list" : queryset
#	}
#	return render(request, template_name, context)
@login_required
def song_votes(request):
	song_id = None
	if request.method == 'GET':
		song_id = request.GET['song_id']
	votes = 0
	if song_id:
		song = Song.objects.filter(id=int(song_id))
		if song:
			votes = song.Votes + 1
			song.Votes = votes
			song.save()
	return HttpResponse(votes)			

class SongListView(LoginRequiredMixin, ListView):
	template_name='songs/songs_list.html'
	def get_queryset(self):
		slug=self.kwargs.get('slug')
		if slug:
			queryset = Song.objects.filter(Genre__icontains=slug).order_by('-Votes','Name')
		else:
			queryset = Song.objects.all().order_by('-Votes','Name')
		return queryset

class GenreListView(LoginRequiredMixin, ListView):
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
	
class SongDetailView(LoginRequiredMixin, DetailView):
	queryset = Song.objects.all()	

class RegisterView(CreateView):
	form_class = RegisterForm
	template_name = "registration/register.html"
	success_url = "/songs/"
#	def get_object(self,*args,**kwargs):
#		song_id = self.kwargs.get('song_id')
#		obj = get_object_or_404(Song,id=song_id)
#		return obj

# class SongCreateView(LoginRequiredMixin,CreateView):
# 	form_class = SongDetailCreateForm
# 	template_name = "songs/form.html"
# 	success_url = "/songs/"
	
# 	def form_valid(self,form):
# 		instance = form.save(commit=False)
# 		instance.owner = self.request.user
# 		return super(SongCreateView,self).form_valid(form)
