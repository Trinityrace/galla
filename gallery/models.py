from __future__ import unicode_literals
from django.db import models

# Create your models here.
# photo model
class Photo(models.Model):
  title = models.CharField(max_length=200)
  width = models.IntegerField(default=0)
  height = models.IntegerField(default=0)
  image = models.ImageField(null=False, blank=False, width_field="width", height_field="height")
  timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

  def __unicode__(self):
    return self.title
    
  class Meta:
    ordering=["-timestamp"]

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

