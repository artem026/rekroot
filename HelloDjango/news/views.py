from django.shortcuts import render, redirect
from . models import Articles
from . forms import ArticlesForm

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news_home.html', {'news': news})

def news_create(request):
    error = ''
    if request.method == 'Post':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Заполните форму правильно'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
        }
    return render(request, 'news_create.html', data)
