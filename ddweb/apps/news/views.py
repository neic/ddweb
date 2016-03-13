from django.views.generic.dates import YearArchiveView, ArchiveIndexView
from django.shortcuts import render

from ddweb.apps.news.models import Article

def newsLatest(request, **kwargs):
    context = {'articles': Article.objects.all().order_by('date')}
    return render(request, 'news.html', context)

class NewsArchive(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "date"
    make_object_list = True
    context_object_name = "articles"
    template_name = 'news.html'
