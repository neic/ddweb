from django.conf.urls import patterns, url

from ddweb.apps.references import views

urlpatterns = patterns('',
                       url(r'^$', 'ddweb.apps.references.views.references',
                           name='references'),
)
