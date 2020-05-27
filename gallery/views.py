from django.shortcuts import render
from .models import Photo
from django.http  import HttpResponse, Http404
import datetime as dt

# Create your views here.
def index(request):
    return render(request, 'photo/base.html')

def gallery(request):
    images = Photo.objects.all().order_by('timestamp')
    return render(request, 'photo/base.html', {'images': images})


def location(request):
    return render(request, 'photo/search.html')


def category(request):
    return render(request, 'photo/base.html')

def search_results(request):
    return render(request, 'photo/search.html')