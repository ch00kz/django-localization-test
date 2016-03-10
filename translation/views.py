from django.shortcuts import render
from django.views.generic import DetailView

from models import Article


def home(request):
    articles = Article.objects.all()
    ctx = {
        'articles': articles
    }
    return render(request, 'home.html', ctx)


class ArticleView(DetailView):
    model = Article
