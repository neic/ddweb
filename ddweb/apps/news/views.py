import os
from django.shortcuts import render
from django.views import generic
from django.views.generic.dates import YearArchiveView, ArchiveIndexView

from ddweb.apps.news.models import Article

class NewsLatest(ArchiveIndexView):
    inner_q = Article.objects.all().values('pk')[0:20]
    queryset = Article.objects.filter(pk__in=inner_q)
    date_field = "date"
    make_object_list = True
    context_object_name = "articles"
    template_name='news.html'

class NewsArchive(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "date"
    make_object_list = True
    context_object_name = "articles"
    template_name='news.html'
