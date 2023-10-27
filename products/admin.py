from django.contrib import admin
from .models import Product, Offer, Gallery


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'description')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'desc', 'file_image_url', 'date_add', 'date_end')
    inlines = [GalleryInline, ]


# Register your models here.
admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
