from django.db import models


def product_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/product_name_<filename>
    return 'product_{0}_{1}'.format(instance.name, filename)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    desc = models.CharField(max_length=2083)
    file_image_url = models.ImageField(upload_to=product_directory_path)
    date_add = models.DateField()
    date_end = models.DateField()


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

