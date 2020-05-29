from django.test import TestCase

# Create your tests here.
# test for categories 
class CategoryTest(TestCase):
    def setUp(self):
        self.art = category(Name='art')

    def test_instance(self):
        self.art.save()
        self.assertTrue(isinstance(self.art, category))

# test for location
class LocationTest(TestCase):
    def setUp(self):
        self.dubai = location(place='dubai')

    def test_instance(self):
        self.dubai.save()
        self.assertTrue(isinstance(self.dubai, location))

