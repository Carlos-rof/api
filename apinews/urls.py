from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('search/', search_results, name='search_results'),
    path('api/v1/get-articles/', get_articles, name='get_articles')
]
