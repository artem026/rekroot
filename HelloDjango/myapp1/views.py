from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index_page(request):
    data = {
        'title': 'Работа мечты',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'job': 'BMW',
            'for': 18,
            'you': 'Football'
        }
    }
    return render(request, 'index.html', data)

@login_required
def about_page(request):
    return render(request, 'about.html')

@login_required
def top_list_page(request):
    return render(request, 'news_top_list.html')

def user_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('home')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')
