from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, world. You're at the chengyu index. Later, you should add a search form here.")

def search(request, query):
  return HttpResponse("You sent the following to the server: %s." % query)