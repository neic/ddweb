from django.shortcuts import render

def newsLatest(request, **kwargs):
    context = {}
    return render(request, 'news.html', context)
