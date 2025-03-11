from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView, ListView
from django.core.files.storage import FileSystemStorage
from .models import Category, Post


class HomeListView(ListView):
    model = Category
    template_name = "article/Home.html"
    context_object_name = "category"


class PostListView(ListView):
    model = Post
    template_name = "article/PostListView.html"
    slug_url_kwarg = 'category_slug'
    context_object_name = "post"

    def get_queryset(self, queryset=None):
        return Post.objects.filter(category__slug=self.kwargs['category_slug'])


class PostDetailView(DetailView):
    model = Post
    template_name = "article/PostDetailView.html"
    pk_url_kwarg = 'id_post'
    context_object_name = "post"