from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
import django.views.static

admin.autodiscover()

urlpatterns = [
    url(r'^$',
        TemplateView.as_view(template_name="company.html"),
        name='company'),
    url(r'^news/',
        include('ddweb.apps.news.urls'),
        name='news'),
    url(r'^contact/',
        TemplateView.as_view(template_name="contact.html"),
        name='contact'),
    url(r'^references/',
        include('ddweb.apps.references.urls'),
        name='references'),
    url(r'^images/',
        include('ddweb.apps.images.urls'),
        name='images'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Temporary media (user uploaded static files) serving from dev server
    url(r'^media/(?P<path>.*)$',
        django.views.static.serve,
        {'document_root': settings.MEDIA_ROOT}),
    ]
