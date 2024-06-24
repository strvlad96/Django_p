from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    context = {
        'players': ['Дамир', 'Арман', 'Рома', 'Влад']
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')