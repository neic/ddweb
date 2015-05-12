from django.conf.urls import patterns, url

from ddweb.apps.news.views import NewsLatest, NewsArchive

urlpatterns = patterns('',
                       url(r'^$', NewsLatest.as_view(),
                           name='news'),
                       url(r'^(?P<year>\d{4})/$', NewsArchive.as_view(),
                           name='news_archive'))
