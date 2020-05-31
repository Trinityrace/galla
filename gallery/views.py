from django.shortcuts import render, get_object_or_404
from .models import Photo, Location, Category
from django.http  import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt

# Create your views here.
# def index(request):
#     images = Photo.objects.all().order_by('timestamp')
#     return render(request, 'photo/gallery.html', {'images': images})

def index(request):
    images = Photo.objects.all()
    location = Location.objects.all()
    category = Category.objects.all()

    if 'location' in request.GET and request.GET['location']:
        name = request.GET.get('location')
        images = Photo.view_locale(name)

    elif 'category' in request.GET and request.GET['category']:
        cart = request.GET.get('category')
        images = Photo.view_category(cart)
        return render(request, 'photo/gallery.html', {"name":name, "images":images, "cart":cart })

    return render(request,"photo/gallery.html",{"images":images,"location":location,"category":category})


def gallery(request):
    images = Photo.objects.all().order_by('timestamp')
    return render(request, 'photo/gallery.html', {'images': images})

def search_results(request):
    if 'Category' in request.GET and request.GET["category"]:
        search_images = request.GET.get("Category")
        searched_images = Photo.search_by_category(search_images)
        message = f"{search_images}"
        return render(request, 'photo/search.html',{"message":message,"photos": searched_images})
    else:
        message = "You haven't searched for an image"    
    return render(request, 'photo/search.html',{"message":message})

def get_image_by_id(request,image_id):
    try:
        image = Photo.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"gallery.html", {"image":image})

def search_by_category(request, category):
    image = Photo.objects.all()
    categorys = Category.objects.all()
    return render(request, 'gallery.html', {"image": image, "categorys": categorys})    

def search_by_locale(request, location):
    locations = Location.objects.all()
    image = Photo.search_by_locale(location)
    return render(request, 'gallery.html', {"image": image, "locations": locations})        

