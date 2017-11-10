from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
# Function based view

def home(request):
	num = random.randint(0,1000)
	some_list = [num,random.randint(0,500),random.randint(0,3000)]
	context = {
		"bool_item" : True,
		"num" : num,
		"some_list" : some_list}
	#return HttpResponse(html_)
	return render(request,"base.html",context)#response 

def home1(request):
	num = random.randint(0,1000)
	some_list = [num,random.randint(0,500),random.randint(0,3000)]
	context = {
		"bool_item" : True,
		"num" : num,
		"some_list" : some_list}
	#return HttpResponse(html_)
	return render(request,"home1.html",context)#response 

def home2(request):
	num = random.randint(0,1000)
	some_list = [num,random.randint(0,500),random.randint(0,3000)]
	context = {
		"bool_item" : True,
		"num" : num,
		"some_list" : some_list}
	#return HttpResponse(html_)
	return render(request,"home2.html",context)#response 

def home3(request):
	num = random.randint(0,1000)
	some_list = [num,random.randint(0,500),random.randint(0,3000)]
	context = {
		"bool_item" : True,
		"num" : num,
		"some_list" : some_list}
	#return HttpResponse(html_)
	return render(request,"home3.html",context)#response 

