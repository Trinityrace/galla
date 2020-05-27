from django.contrib import admin
from .models import Photo, Category, Location

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
  list_display = ["title","timestamp"]

  class Meta:
    model = Photo

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Location)
admin.site.register(Category)