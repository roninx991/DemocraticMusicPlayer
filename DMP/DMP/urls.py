"""DMP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from songs.views import SongListView,GenreListView,SongDetailView,signup,login_user
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',signup),
    url(r'^login/$',login_user,name="login"),
    url(r'^songs/$',SongListView.as_view(),name="songs"),
    url(r'^songs/(?P<slug>[\w-]+)/$',SongDetailView.as_view()),
    url(r'^genre/$',GenreListView.as_view(),name="genre"),
    url(r'^genre/(?P<slug>\w+)/$',SongListView.as_view()),
    url(r'^about/$',TemplateView.as_view(template_name="about.html"),name="about"),
    url(r'^contact/$',TemplateView.as_view(template_name="contact.html"),name="contact"),
]
