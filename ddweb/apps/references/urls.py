from django.conf.urls import url

from ddweb.apps.references.views import references

urlpatterns = [
    url(r'^$', references,
        name='references')
    ]
