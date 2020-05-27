from __future__ import unicode_literals
from django.db import models
import datetime as dt

# Create your models here.
Default_description = "Photographical Art At Its Best!"
# photo model
class Photo(models.Model):
  title = models.CharField(max_length=70)
  width = models.IntegerField(default=0)
  height = models.IntegerField(default=0)
  image = models.ImageField(null=False, blank=False, width_field="width", height_field="height", default='default.jpg')
  timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
  descripion = models.TextField(default=Default_description)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  taken_by = models.CharField(max_length=20, blank=True)

  def __unicode__(self):
    return self.title
    
  class Meta:
    ordering=["-timestamp"]

  @classmethod    
  def save_image(self):
      self.save()

  @classmethod
  def delete_image(self):
      self.delete()

  @classmethod
  def update_image(cls, id, value):
      cls.objects.filter(id=id).update(value)

  @classmethod
  def get_image_by_id(cls, id):
      return cls.objects.get(pk=id)

  @classmethod
  def search_by_category(cls,search_term):
    search_results = cls.objects.filter(category__Name__icontains=search_term)
    return search_results

  @classmethod
  def search_by_location(cls, search_term):
      photo = Photo.objects.filter(location__id=search_term).all()
      return photo


# location class and methods
class Location():
  place = models.CharField(max_length=30)

  def __str__(self):
      return self.place

  @classmethod
  def save_location(self):
      self.save()
  
  @classmethod 
  def delete_location(self):
      self.delete()
      
  @classmethod
  def update_location(cls, id, new_location):
      cls.objects.filter(id=id).update(location=new_location) 

# category class and methods
class Category(models.Model):
  Name = models.CharField(max_length=30)

  def __str__(self):
    return self.Name

  @classmethod
  def save_category(self):
      self.save()
      
  @classmethod
  def delete_category(self):
      self.delete()
      
  @classmethod
  def update_category(cls, id, new_category):
      cls.objects.filter(id=id).update(Category=new_category)

