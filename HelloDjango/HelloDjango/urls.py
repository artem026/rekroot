"""
URL configuration for HelloDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp1.views import index_page, about_page,top_list_page, user_login, user_logout
from news.views import news_pagination

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='home'),
    path('about/', about_page, name='about'),
    path('news/', include('news.urls')),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('top_list/', top_list_page, name='top_list'),
    path('pagination/', news_pagination, name='news_pagination')
]
