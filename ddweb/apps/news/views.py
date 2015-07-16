from django.views.generic.dates import YearArchiveView, ArchiveIndexView

from ddweb.apps.news.models import Article

class NewsLatest(ArchiveIndexView):
    queryset = Article.objects.all().order_by('date')
    date_field = "date"
    make_object_list = True
    context_object_name = "articles"
    template_name = 'news.html'

class NewsArchive(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "date"
    make_object_list = True
    context_object_name = "articles"
    template_name = 'news.html'
