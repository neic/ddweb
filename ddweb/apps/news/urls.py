from django.conf.urls import url

from ddweb.apps.news.views import newsLatest

urlpatterns = [
    url(r'^$', newsLatest,
        name='news'),
    ]
