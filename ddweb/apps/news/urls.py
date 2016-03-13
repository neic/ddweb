from django.conf.urls import patterns, url

from ddweb.apps.news.views import NewsArchive

urlpatterns = patterns('',
                       url(r'^$', 'ddweb.apps.news.views.newsLatest',
                           name='news'),
                       url(r'^(?P<year>\d{4})/$', NewsArchive.as_view(),
                           name='news_archive'))
