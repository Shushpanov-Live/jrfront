from django.urls import path
from . import views

urlpatterns = [
    path('', views.lk, name='lk'),
    path('lk-pass/', views.lk_Pass, name='lk-pass'),
    path('lk-pass/rep-pass/', views.rep_pass, name='rep-pass'),
]