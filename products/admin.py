from django.contrib import admin
from .models import Product, Offer, Gallery, Pages


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


class OfferInline(admin.TabularInline):
    fk_name = 'product'
    model = Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'description')


class PagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'desc', 'date_add', 'date_end')
    inlines = [GalleryInline, OfferInline]


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image', 'product')


# Register your models here.
admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Pages, PagesAdmin)
