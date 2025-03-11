from django.shortcuts import render


def lk(request):
    return render(request, 'lkSite/lk.html',)


def lk_Pass(request):
    return render(request, 'lkSite/password.html')


def rep_pass(request):
    return render(request, 'lkSite/replace.html')