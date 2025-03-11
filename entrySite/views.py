from django.shortcuts import render


def entry(request):
    return render(request, 'entrySite/entry.html',)
