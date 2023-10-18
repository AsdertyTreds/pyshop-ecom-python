from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products,
                   'url': request.build_absolute_uri()})


def new(request):
    products = Product.objects.all()
    return render(request, 'news.html',
                  {'products': products,
                   'url': request.build_absolute_uri()})


def item(request, name):
    try:
        product = Product.objects.get(name=name)
        return render(request, 'item.html',
                      {'product': product,
                       'url': request.build_absolute_uri()})

    except ObjectDoesNotExist:
        products = Product.objects.all()
        return render(request, 'index.html',
                      {'products': products})
