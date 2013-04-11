from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ddweb.views.home', name='home'),
    url(r'^references/', 'ddweb.apps.references.views.references'),
    url(r'^ongoing/', 'ddweb.apps.references.views.ongoing'),
    url(r'^news/', 'ddweb.apps.news.views.news'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Temporary media (user uploaded static files) serving from dev server
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
