from django.shortcuts import render
# Create your views here.
data = {'title': 'Главная страница',
        'objects': ['Добро пожаловать', 'Как дела', 'Что будете делать?']
        }
def index(request):
    return render(request, "main/index.html", data)
def about(request):
    return render(request, "main/about.html", {'title': 'О нас'})
def contact(request):
    return render(request, "main/contact.html", {'title': 'Контакты'})
