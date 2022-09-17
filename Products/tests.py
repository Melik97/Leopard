from unicodedata import category
from django.test import TestCase
from .models import Product, Category

class ProductTestCase(TestCase):
    def setUp(self):
        category.objects.create()
        Product.objects.create(name="lion", sound="roar")
        Product.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Product.objects.get(name="lion")
        cat = Product.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')