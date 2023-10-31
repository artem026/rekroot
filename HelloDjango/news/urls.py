from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.news_create, name='news_create')
]