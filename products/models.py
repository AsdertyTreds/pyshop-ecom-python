from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


def product_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/product_name_<filename>
    return 'product_{0}_{1}'.format(instance.name, filename)


class Product(models.Model):
    """ Модель продукция """
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(_("Name"), max_length=255)
    price = models.FloatField(_("Price"))
    stock = models.IntegerField(_("Count"))
    desc = models.TextField(_("Description"), max_length=2083)
    file_image_url = models.ImageField(_("Image"), upload_to=product_directory_path)
    date_add = models.DateTimeField(_("Date add"), auto_now=True)
    date_end = models.DateTimeField(_("Date off"))

    class Meta:
        verbose_name = _("Florarium")
        verbose_name_plural = _("Florariums")
        ordering = ['-date_add']

    def __str__(self):
        """String for representing the ModelName object (in Admin site etc.)."""
        return self.name


class Offer(models.Model):
    """ Модель скидок """
    code = models.CharField(_("Promo"), max_length=10)
    description = models.CharField(_("Description"), max_length=255)
    discount = models.FloatField(_("Size in %"))

    class Meta:
        verbose_name = _('Discount')
        verbose_name_plural = _('Discounts')


class Gallery(models.Model):
    image = models.ImageField(_("Image"),upload_to='product_directory_path')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')