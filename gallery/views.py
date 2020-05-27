from django.shortcuts import render
from .models import Photo
from django.http  import HttpResponse, Http404
import datetime as dt

# Create your views here.
def index(request):
    return render(request, 'photo/base.html')

def gallery(request):
    images = Photo.objects.all().order_by('timestamp')
    return render(request, 'photo/gallery.html', {'images': images})


def location(request):
    return render(request, 'photo/search.html')


def category(request):
    return render(request, 'photo/base.html')

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Photo.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'photo/search.html',{"message":message,"photos": searched_images})

    else:
        message = "You haven't searched for any term"    
    return render(request, 'photo/search.html',{"message":message})