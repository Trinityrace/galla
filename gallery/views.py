from django.shortcuts import render
from .models import Photo
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    queryset = Photo.objects.all()
    context = {
        "photos" = queryset,
    }
    return render(request,'templates', content)
