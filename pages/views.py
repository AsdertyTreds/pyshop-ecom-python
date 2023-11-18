from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Pages


def contacts1(request):
    return render(request, 'contacts.html',
                  {'ogurl': request.build_absolute_uri()})


def howtoorder(request):
    return render(request, 'howtoorder.html',
                  {'ogurl': request.build_absolute_uri()})


class Contacts(ListView):
    model = Pages
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = Pages.objects.get(name="contacts")
        context["ogurl"] = self.request.build_absolute_uri()
        return context
