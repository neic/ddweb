from django.conf.urls import patterns, url
from django.views.generic.dates import ArchiveIndexView

from ddweb.apps.news import views
from ddweb.apps.news.views import NewsLatest, NewsArchive

urlpatterns = patterns('',
                       url(r'^$', NewsLatest.as_view(),
                           name='news'),
                       url(r'^(?P<year>\d{4})/$', NewsArchive.as_view(),
                           name='news_archive'),
)
