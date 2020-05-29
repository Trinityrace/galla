from django.test import TestCase
from .models import Location, Category, Photo

# Create your tests here.
# test for categories 
class CategoryTest(TestCase):
    def setUp(self):
        self.art = Category(Name='art')

    def test_instance(self):
        self.art.save()
        self.assertTrue(isinstance(self.art, Category))

# test for location
class LocationTest(TestCase):
    def setUp(self):
        self.dubai = Location(place='dubai')

    def test_instance(self):
        self.dubai.save()
        self.assertTrue(isinstance(self.dubai, Location))

