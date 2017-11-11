from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
import random
# Create your views here.
# Function based view

class HomeView(TemplateView):
	template_name = "home.html"
	def get_context_data(self, *args, **kwargs):
		context = super(HomeView,self).get_context_data(*args,**kwargs)
		num = None
		bool_item = True
		if bool_item :
			num = random.randint(0,3500)
		some_list = [
			random.randint(0,10000),
			random.randint(0,20000),
			random.randint(0,1000),
			]
		context = {
			"some_list" : some_list,
			"num" : num,
			}
		return context


