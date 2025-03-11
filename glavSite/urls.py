from django.urls import path
from django.urls import path, include
from django.views.generic import ListView, DetailView
from glavSite.models import Article
from . import views


app_name = 'glavSite'

urlpatterns = [
    path('', views.BulletinListView.as_view(), name='BulletinListView'),
]

