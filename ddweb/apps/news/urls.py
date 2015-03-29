from django.conf.urls import patterns, url
from django.views.generic.dates import ArchiveIndexView

from ddweb.apps.news import views
from ddweb.apps.news.views import NewsLatest, NewsArchive

urlpatterns = patterns('',
                       url(r'^$', NewsLatest.as_view(),
                           name='news'),
                       url(r'^(?P<year>\d{4})/$', NewsArchive.as_view(),
                           name='news_archive'),
                       url(r'^upload/', 'ddweb.apps.news.views.upload',
                           name = 'jfu_upload' ),
                       url(r'^delete/(?P<pk>\d+)$', 'ddweb.apps.news.views.upload_delete',
                           name = 'jfu_delete' ),
                       url(r'^uploadf/(?P<article_id>\w+)', 'ddweb.apps.news.views.newsImgUpload',
                           name = 'uploadform' ),

)
