from django.conf.urls import url

from ddweb.apps.news.views import newsLatest, NewsArchive

urlpatterns = [
    url(r'^$', newsLatest,
        name='news'),
    url(r'^(?P<year>\d{4})/$', NewsArchive.as_view(),
        name='news_archive')
    ]
