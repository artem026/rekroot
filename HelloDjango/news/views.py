from django.shortcuts import render, redirect
from . models import Articles
from . forms import ArticlesForm
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news_details.html'
    context_object_name = 'article'

@login_required
def news_create(request):
    error = ''
    if request.method == 'POST':
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


def news_pagination(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news_pagination.html', {'news': news})
