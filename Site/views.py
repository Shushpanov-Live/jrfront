from django.shortcuts import render


def index(request):
    return render(request, 'Site/site.html',)

def twoopen(request):
    return render(request, 'Site/twoopen.html',)

def tel_bot(request):
    return render(request, 'Site/tel_bot.html',)