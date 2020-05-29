from django.test import TestCase
from .models import Location, Category, Photo

# Create your tests here.
# test for category 
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

### Photo class tests

class PhotoTest(TestCase):

    def setUp(self):
        self.dubai = Location.objects.create(name='dubai')
        self.fun = Category.objects.create(name='fun')
        self.art = Category.objects.create(name='art')

        self.juice = Photo.objects.create(
            title='juice', location=self.dubai,  description='picture of a juice')

        self.juice.category.add(self.fun)
        self.juice.category.add(self.music)

    def test_instance(self):
        self.juice.save()
        self.assertTrue(isinstance(self.juice, Photo))

    def test_delete_image(self):
        self.juice.save()
        self.juice.delete()
        self.assertTrue(len(Photo.objects.all()) == 0)

    def test_update(self):
        self.juice.save()
        self.juice.name = 'MoreJuices'
        self.assertTrue(self.juice.name == 'MoreJuices')

    def test_all_images(self):
        self.juice.save()
        images = Photo.all_images()
        self.assertTrue(len(images) > 0)

    def test_search_by_id(self):
        self.juice.save()
        images = Photo.search_by_id('fun')
        self.assertTrue(len(images) > 0)

    def test_search_by_location(self):
        self.juice.save()
        location = Photo.search_by_location(self.dubai)
        self.assertTrue(len(location) > 0)

    def test_search_by_category(self):
        self.juice.save()
        category = Photo.search_by_category(self.art)
        self.assertTrue(len(category) > 0)
