from django.http import HttpResponse
from ddweb_app.models import Reference

def index(request):
    rList = Reference.objects.all()
    output = rList
    return HttpResponse(output)
