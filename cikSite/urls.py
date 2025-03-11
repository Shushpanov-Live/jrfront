from django.urls import path
from django.urls import path, include
from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
    path('', views.cik, name='cik'),
    path('newwapon/', views.newwapon, name='newwapon'),
    path('dogovordog/', views.dogovordog, name='dogovordog'),
    path('raspiska_o_zaeme/', views.raspiska_o_zaeme, name='raspiska'),
    path('doverennost/', views.doverennost, name='doverennost'),
    path('akt_vypolnennyh_rabot/', views.akt_vypolnennyh_rabot, name='akt_vypolnennyh_rabot'),
    path('spravka/', views.spravka, name='spravka'),
    path('comparison/', views.comparison, name='comparison'),
]
