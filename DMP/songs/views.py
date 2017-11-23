from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView
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
			login(request, user)
			for s in queryset:
				vote = request.POST.get(s.slug)
				if vote:
					obj = get_object_or_404(Song,id=s.id)
					obj.Votes = obj.Votes + 1
					obj.save()

		
			return redirect('/songs/')
	else:
		form = UserCreationForm()
	return render(request, 'home.html', {'form': form,'songs':queryset})

def login_user(request):
	if request.method == 'POST':
		user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
		if user:
			login(request,user)
			return redirect('/songs/')
	form = AuthenticationForm()
	return render(request, 'registration/login.html',{'form':form})

class SongListView(LoginRequiredMixin, ListView):
	template_name='songs/songs_list.html'
	redirect_field_name = '/songs/'
	def get_queryset(self):
		slug=self.kwargs.get('slug')
		if slug:
			queryset = Song.objects.filter(Genre__icontains=slug).order_by('-Votes','Name')
		else:
			queryset = Song.objects.all().order_by('-Votes','Name')
		return queryset

class GenreListView(LoginRequiredMixin, ListView):
	template_name='songs/genres_list.html'
	redirect_field_name = '/genres/'
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