from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('gallery/', views.gallery, name='gallery'),
    url('category/', views.category, name='category'),
    url('search/', views.search_results, name='search_results'),
    url('location/', views.location, name='location'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)