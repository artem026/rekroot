from django.shortcuts import render

def index_page(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'index.html', data)

def about_page(request):
    return render(request, 'about.html')
