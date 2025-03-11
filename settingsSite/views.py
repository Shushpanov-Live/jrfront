from django.shortcuts import render


def settings(request):
    return render(request, 'settingsSite/settings.html',)

def developer(request):
    return render(request, 'settingsSite/developer.html',)

def partners(request):
    return render(request, 'settingsSite/partners.html',)

def fiz_face(request):
    return render(request, 'settingsSite/legal_face.html',)

def legal_face(request):
    return render(request, 'settingsSite/fiz_face.html',)