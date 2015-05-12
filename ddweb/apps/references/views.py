from django.shortcuts import render

from ddweb.apps.references.models import Reference

def references(request):
    ongoing = Reference.objects.filter(ongoing=True)
    finished = Reference.objects.filter(ongoing=False, beforeDD=False)
    before = Reference.objects.filter(beforeDD=True)
    context = {'ongoing': ongoing,
               'finished': finished,
               'before': before}
    return render(request, 'references.html', context)
