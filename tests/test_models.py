from django.test import TestCase
from products.models import product_directory_path
from collections import namedtuple
from django.db import models
from products.models import Product
from products.models import Offer
from django.utils.translation import gettext_lazy as _


class TestProductDirectoryPath(TestCase):
    def test_product_directory_path(self):
        print("Method: product_directory_path.")
        test_instance = namedtuple('name', 'name')
        test_instance.name = 'name'
        test_filename = 'filename'
        self.assertEqual(product_directory_path(test_instance, test_filename), 'product_name_filename')


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name='Flo', price=1000, stock=1, desc='test description',
                               file_image_url='Flo.jpg', date_add='2023-10-01', date_end='2023-10-31')

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, _('name'))

    def test_first_name_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)
