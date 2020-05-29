from django.test import TestCase
from .models import Location, Category, Photo

# Create your tests here.
# test for category 
class CategoryTest(TestCase):
  # creating new category and saving
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
        self.dubai = Location.objects.create(place='dubai')
        self.fun = Category.objects.create(Name='fun')
        self.art = Category.objects.create(Name='art')

        self.juice = Photo.objects.create(
            title='juice', location=self.dubai, descripion='picture of a juice')

        self.juice.category.add(self.fun)
        self.juice.category.add(self.art)

    def test_instance(self):
        self.juice.save()
        self.assertTrue(isinstance(self.juice, Photo))

    def test_save_image(self):
        self.juice.save()
        images= Photo.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        self.juice.save()
        self.juice.delete()
        self.assertTrue(len(Photo.objects.all()) == 0)

    def test_update(self):
        self.juice.save()
        self.juice.title = 'MoreJuices'
        self.assertTrue(self.juice.title == 'MoreJuices')

    def test_search_results(self):
        self.juice.save()
        # search_results = Photo.view_category(search_image)
        # self.assertTrue(len(search_results)==0)
        images = Photo.search_results('fun')
        self.assertTrue(len(images)>0)

    def test_search_by_locale(self):
        self.juice.save()
        #images = Photo.get_image_by_id(int(id))
        search_by_locale= Location.get(id)
        self.assertTrue(len(search_by_locale)>0)

    def test_view_locale(self):
        self.juice.save()
        locale = Photo.view_locale(self.dubai)
      #  search_by_location = Location.get(id)
        self.assertTrue(len(locale)>0)

    def test_view_category(self):
        self.juice.save()
        category = Photo.view_category(self.fun)
        self.assertTrue(len(category) > 0)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Photo.objects.all().delete()