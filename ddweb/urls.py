from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ddweb.views.home', name='home'),
                       url(r'^$', TemplateView.as_view(template_name="company.html"), name = 'company'),
                       url(r'^news/', 'ddweb.apps.news.views.news', name = 'news'),
                       url(r'^contact/', TemplateView.as_view(template_name="contact.html"), name = 'contact'),
                       url(r'^ongoing/', 'ddweb.apps.references.views.ongoing', name = 'ongoing'),
                       url(r'^references/', 'ddweb.apps.references.views.references', name = 'references'),
                       url(r'upload/', 'ddweb.apps.news.views.upload', name = 'jfu_upload' ),
                       url( r'^delete/(?P<pk>\d+)$', 'ddweb.apps.news.views.upload_delete', name = 'jfu_delete' ),
                       url(r'uploadf/(?P<article_id>\w+)', 'ddweb.apps.news.views.newsImgUpload', name = 'uploadform' ),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Temporary media (user uploaded static files) serving from dev server
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
