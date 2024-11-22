from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  context = {'title' : "Daftar Product"}
  return render(request, 'index.html', context)

# Create your views here.
