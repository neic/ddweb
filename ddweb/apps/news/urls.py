from django.conf.urls import patterns, url

from ddweb.apps.news import views

urlpatterns = patterns('',
                       url(r'^$', 'ddweb.apps.news.views.news',
                           name='news'),
                       url(r'^upload/', 'ddweb.apps.news.views.upload',
                           name = 'jfu_upload' ),
                       url(r'^delete/(?P<pk>\d+)$', 'ddweb.apps.news.views.upload_delete',
                           name = 'jfu_delete' ),
                       url(r'^uploadf/(?P<article_id>\w+)', 'ddweb.apps.news.views.newsImgUpload',
                           name = 'uploadform' ),

)
