from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def index(request):
    news = Articles.objects.order_by('-date')
    return render(request, "news/news_home.html", {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_news.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/update_news.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/delete_news.html'
    success_url = '/news'
    form_class = ArticlesForm


def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Данные не верны.'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, "news/create_news.html", data)