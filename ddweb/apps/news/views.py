import os
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.decorators.http import require_POST
from jfu.http import upload_receive, UploadResponse, JFUResponse

from ddweb.apps.news.models import Article, ArticleImage

def news(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'news.html', context)

@permission_required('news.add_articleimage')
def newsImgUpload(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {'article_id' : article_id,
               'article_name' : str(article) }
    return render(request, 'news-img-upload.html', context)

@require_POST
@permission_required('news.add_articleimage', raise_exception=True)
def upload(request):

    # The assumption here is that jQuery File Upload
    # has been configured to send files one at a time.
    # If multiple files can be uploaded simulatenously,
    # 'file' may be a list of files.
    image = upload_receive(request)
    article_id = request.POST['article_id']
    article = get_object_or_404(Article, id=article_id)
    instance = ArticleImage(image = image, article = article)
    instance.save()

    basename = os.path.basename(instance.image.path)

    file_dict = {
        'name' : basename,
        'size' : image.size,

        'url': instance.image.url,
        'thumbnailUrl': instance.thumbnail.url,

        'deleteUrl': reverse('jfu_delete', kwargs = { 'pk': instance.pk }),
        'deleteType': 'POST',
    }

    return UploadResponse(request, file_dict)

@require_POST
@permission_required('news.add_articleimage', raise_exception=True)
def upload_delete( request, pk ):
    success = True
    try:
        instance = ArticleImage.objects.get( pk = pk )
        os.unlink( instance.image.path )
        os.unlink( instance.thumbnail.path )
        instance.delete()
    except ArticleImage.DoesNotExist:
        success = False

    return JFUResponse( request, success )
