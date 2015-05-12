import os
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.decorators.http import require_POST
from jfu.http import upload_receive, UploadResponse, JFUResponse

from ddweb.apps.references.models import Reference

def references(request):
    ongoing = Reference.objects.filter(ongoing = True)
    references = Reference.objects.filter(ongoing = False, beforeDD = False)
    before = Reference.objects.filter(beforeDD = True)
    context = {'ongoing': ongoing,
               'references': references,
               'before': before}
    return render(request, 'references.html', context)
