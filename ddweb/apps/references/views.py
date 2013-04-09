from django.shortcuts import render
from ddweb.apps.references.models import Reference

def index(request):
    references = Reference.objects.all()
    context = {'references': references}
    return render(request, 'references.html', context)
