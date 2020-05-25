from django.shortcuts import render
from .models import Photo
from django.http  import HttpResponse, Http404

# Create your views here.
def index(request):
    images = Photo.objects.all().order_by('timestamp')
    return render(request, 'photo/photo.html', {'images': images})
