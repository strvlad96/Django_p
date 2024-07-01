from django.shortcuts import render
from .models import Articles


# Create your views here.

def index(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news.html', {'news': news})