from django.http import HttpResponse
from ddweb.apps.references.models import Reference

def index(request):
    rList = Reference.objects.all()
    output = rList
    return HttpResponse(output)
