from django.urls import path
from django.urls import path, include
from django.views.generic import ListView, DetailView
from article.models import Category, Post
from . import views


app_name = 'article'

urlpatterns = [
    #path('', ListView.as_view(queryset=Category.objects.order_by('title'), template_name="article/test.html")),
    #path('', views.mainBulletin, name='test'),
    #path('', views.mainBulletin, name='test'),
    #path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    #path('<slug:category_slug>/<int:id>/', views.content, name='content'),


    path('', views.HomeListView.as_view(), name='HomeListView'),
    path('<slug:category_slug>/', views.PostListView.as_view(), name='PostListView'),
    path('<slug:category_slug>/<int:id_post>/', views.PostDetailView.as_view(), name='PostDetailView'),
]