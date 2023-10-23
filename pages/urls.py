from django.urls import path
from . import views


urlpatterns = [
    path('', views.howtoorder, name='howtoorder'),
    path('contacts/', views.contacts, name='contacts'),
    path('howtoorder/', views.howtoorder, name='howtoorder')
]
