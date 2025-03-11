from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView, ListView
from django.core.files.storage import FileSystemStorage
from .models import Article

class BulletinListView(ListView):
    model = Article
    template_name = "glavSite/bulletin.html"
    context_object_name = "bulletin"

    


#class VoteDetailView(DetailView):
    #model = Article
    #template_name = "glavSite/vote.html"
    #context_object_name = "article"

