from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

def index(request):
  template = loader.get_template('meow.html')
  word = request.GET.get('word', "?Word=''")
  context = {
    'word': word
  }
  return HttpResponse(template.render(context, request))