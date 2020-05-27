from django.shortcuts import render
from .models import Photo
from django.http  import HttpResponse, Http404
import datetime as dt

# Create your views here.
def index(request):
    images = Photo.objects.all().order_by('timestamp')
    return render(request, 'photo/base.html', {'images': images})


def location():
    return render(request)


def category():
    return render(request, 'photo/category.html')

def search_image_by_id(id):
    return render(request, 'photo/search.html')