from django.conf.urls import patterns, url

from ddweb.apps.references import views

urlpatterns = patterns('',
                       url(r'^$', 'ddweb.apps.references.views.references',
                           name='references'),
                       url(r'^upload/', 'ddweb.apps.references.views.upload',
                           name = 'jfu_upload' ),
                       url(r'^delete/(?P<pk>\d+)$', 'ddweb.apps.references.views.upload_delete',
                           name = 'jfu_delete' ),
                       url(r'^uploadf/(?P<reference_id>\w+)', 'ddweb.apps.references.views.refImgUpload',
                           name = 'uploadform' ),

)
