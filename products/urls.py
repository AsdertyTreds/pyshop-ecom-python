from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('news/', views.News.as_view(), name='news'),
    path('item/<int:id>', views.item, name='item'),
    path('search/', views.SearchResult.as_view(), name='search_result')
]
