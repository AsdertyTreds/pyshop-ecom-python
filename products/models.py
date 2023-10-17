from django.db import models


def product_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/product_name_<filename>
    return 'product_{0}_{1}'.format(instance.name, filename)


class Product(models.Model):
    """ Модель продукция """
    name = models.CharField("Название", max_length=255)
    price = models.FloatField("Цена")
    stock = models.IntegerField("Количество")
    desc = models.TextField("Описание", max_length=2083)
    file_image_url = models.ImageField("Изображение", upload_to=product_directory_path)
    date_add = models.DateField("Дата создания", auto_now=True)
    date_end = models.DateField("Дата окончания")

    class Meta:
        verbose_name = 'Флорариум'
        verbose_name_plural = 'Флорариумы'

    def __str__(self):
        """String for representing the ModelName object (in Admin site etc.)."""
        return self.name

class Offer(models.Model):
    """ Модель скидок """
    code = models.CharField("Промокод", max_length=10)
    description = models.CharField("Описание", max_length=255)
    discount = models.FloatField("Размер, в %")

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'