from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from django.core.exceptions import ObjectDoesNotExist


class Index(ListView):
    model = Product
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        context["ogurl"] = self.request.build_absolute_uri()
        return context


class News(ListView):
    model = Product
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        context["ogurl"] = self.request.build_absolute_uri()
        return context


def item(request, id):
    try:
        product = Product.objects.get(id=id)
        images = product.images.all()
        return render(request, 'item.html',
                      {'product': product,
                       'ogurl': request.build_absolute_uri(),
                       'images': images})

    except ObjectDoesNotExist:
        products = Product.objects.all()
        return render(request, 'index.html',
                      {'products': products})


class SearchResult(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        products = Product.objects.filter(desc__icontains=query) if query is not None else Product.objects.all()
        return products
