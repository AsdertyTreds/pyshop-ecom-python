from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products,
                   'ogurl': request.build_absolute_uri()})


class News(ListView):
    model = Product
    template_name = 'index.html'

    def get_queryset(self):  # news
        products = Product.objects.all()
        return {'products': products,
                'ogurl': self.request.build_absolute_uri()}


def news(request):
    products = Product.objects.all()
    return render(request, 'news.html',
                  {'products': products,
                   'ogurl': request.build_absolute_uri()})


def item(request, id):
    try:
        product = Product.objects.get(id=id)
        return render(request, 'item.html',
                      {'product': product,
                       'ogurl': request.build_absolute_uri()})

    except ObjectDoesNotExist:
        products = Product.objects.all()
        return render(request, 'index.html',
                      {'products': products})


class SearchResult(ListView):
    model = Product
    template_name = 'search.html'
    context_object_name = 'products'
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        products = Product.objects.filter(desc__icontains=query) if query is not None else Product.objects.all()
        return products
