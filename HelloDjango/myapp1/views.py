from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def index_page(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'job': 'BMW',
            'for': 18,
            'you': 'Football'
        }
    }
    return render(request, 'index.html', data)

def about_page(request):
    return render(request, 'about.html')

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
    pass
