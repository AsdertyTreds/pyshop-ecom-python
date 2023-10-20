from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products,
                   'url': request.build_absolute_uri()})


def news(request):
    products = Product.objects.all()
    return render(request, 'news.html',
                  {'products': products,
                   'url': request.build_absolute_uri()})


def item(request, id):
    try:
        product = Product.objects.get(id=id)
        return render(request, 'item.html',
                      {'product': product,
                       'url': request.build_absolute_uri()})

    except ObjectDoesNotExist:
        products = Product.objects.all()
        return render(request, 'index.html',
                      {'products': products})
