from django.shortcuts import render
from . models import Articles

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news_home.html', {'news': news})

def news_create(request):
    return render(request, 'news_create.html')
