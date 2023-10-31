from django.shortcuts import render
from . models import Articles
from . forms import ArticlesForm

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news_home.html', {'news': news})

def news_create(request):
    form = ArticlesForm()
    data = {'form': form}
    return render(request, 'news_create.html', data)
