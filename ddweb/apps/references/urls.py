from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'ddweb.apps.references.views.references',
                           name='references'))
