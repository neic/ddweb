from django.shortcuts import render
from ddweb.apps.references.models import Reference

def references(request):
    ongoing = Reference.objects.filter(ongoing = True)
    references = Reference.objects.filter(ongoing = False, beforeDD = False)
    before = Reference.objects.filter(beforeDD = True)
    context = {'ongoing': ongoing,
               'references': references,
               'before': before}
    return render(request, 'references.html', context)
