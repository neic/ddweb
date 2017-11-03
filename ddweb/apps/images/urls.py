from django.conf.urls import url

from ddweb.apps.images.views import upload, upload_delete, uploadForm

urlpatterns = [
    url(r'^upload/',
        upload,
        name='jfu_upload'),
    url(r'^delete/(?P<pk>\d+)$',
        upload_delete,
        name='jfu_delete'),
    url(r'^uploadf/(?P<content_type>\w+)/(?P<object_id>\w+)',
        uploadForm,
        name='uploadform')
    ]
