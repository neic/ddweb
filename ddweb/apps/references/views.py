from django.shortcuts import render
from ddweb.apps.references.models import Reference

def index(request):
    rList = Reference.objects.all()
    context = {'rList': rList}
    return render(request, 'references.html', context)
