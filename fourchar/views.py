from django import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context, loader

from .models import Chengyu

def index(request):
  most_common_chengyus = Chengyu.objects.exclude(chengyu_translation='').order_by('z_rarity')[:5]
  template = loader.get_template('fourchar/index.html')
  context = {
    'most_common_chengyus': most_common_chengyus,
  }
  return HttpResponse(template.render(context, request))
  # return HttpResponse("Hello, world. You're at the chengyu index. Later, you should add a search form here.")

def search(request, query):
  return HttpResponse("You sent the following to the server: %s." % query)