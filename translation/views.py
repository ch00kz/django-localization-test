from django.shortcuts import render
from django.views.generic import DetailView, CreateView

from models import Article


def home(request):
    articles = Article.objects.all()
    ctx = {
        'articles': articles
    }
    return render(request, 'home.html', ctx)


class ArticleView(DetailView):
    model = Article


class AuthorCreate(CreateView):
    model = Article
    fields = ['title', 'content']
