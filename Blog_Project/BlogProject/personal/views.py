from django.shortcuts import render, get_object_or_404
from .models import Article


def all_blogs(request):
    articles = Article.objects.all()
    return render(request, 'personal/all_blogs.html', {'articles': articles})


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'personal/detail.html', {"article": article})
