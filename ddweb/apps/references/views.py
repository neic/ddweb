import os
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.decorators.http import require_POST
from jfu.http import upload_receive, UploadResponse, JFUResponse

from ddweb.apps.references.models import Reference, ReferenceImage

def references(request):
    ongoing = Reference.objects.filter(ongoing = True)
    references = Reference.objects.filter(ongoing = False, beforeDD = False)
    before = Reference.objects.filter(beforeDD = True)
    context = {'ongoing': ongoing,
               'references': references,
               'before': before}
    return render(request, 'references.html', context)


@permission_required('news.add_articleimage')
def refImgUpload(request, reference_id):
    reference = get_object_or_404(Reference, id=reference_id)
    context = {'reference_id' : reference_id,
               'reference_name' : str(reference) }
    return render(request, 'ref-img-upload.html', context)

@require_POST
@permission_required('news.add_articleimage', raise_exception=True)
def upload(request):

    # The assumption here is that jQuery File Upload
    # has been configured to send files one at a time.
    # If multiple files can be uploaded simulatenously,
    # 'file' may be a list of files.
    image = upload_receive(request)
    reference_id = request.POST['reference_id']
    reference= get_object_or_404(Reference, id=reference_id)
    instance = ReferenceImage(image = image, reference = reference)
    instance.save()

    basename = os.path.basename(instance.image.path)

    file_dict = {
        'name' : basename,
        'size' : image.size,

        'url': instance.image.url,

        'deleteUrl': reverse('jfu_delete', kwargs = { 'pk': instance.pk }),
        'deleteType': 'POST',
    }

    return UploadResponse(request, file_dict)

@require_POST
@permission_required('news.add_articleimage', raise_exception=True)
def upload_delete( request, pk ):
    success = True
    try:
        instance = ReferenceImage.objects.get( pk = pk )
        os.unlink( instance.image.path )
        instance.delete()
    except ReferenceImage.DoesNotExist:
        success = False

    return JFUResponse( request, success )
