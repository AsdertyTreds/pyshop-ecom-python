from django.http import HttpResponse
from django.shortcuts import render


def contacts(request):
    return render(request, 'contacts.html',
                  {'ogurl': request.build_absolute_uri()})


def howtoorder(request):
    return render(request, 'howtoorder.html',
                  {'ogurl': request.build_absolute_uri()})
