from django.conf.urls import patterns, url

from ddweb.apps.news import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
