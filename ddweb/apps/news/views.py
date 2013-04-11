from django.shortcuts import render
from ddweb.apps.news.models import Article

def news(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'news.html', context)
