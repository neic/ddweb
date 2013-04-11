from django.shortcuts import render
from ddweb.apps.references.models import Reference

def references(request):
    references = Reference.objects.filter(ongoing = False)
    context = {'references': references}
    return render(request, 'references.html', context)

def ongoing(request):
    references = Reference.objects.filter(ongoing = True)
    context = {'references': references}
    return render(request, 'references.html', context)
