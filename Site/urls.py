from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tel-bot/', views.tel_bot, name='tel_bot'),
    path('twoopen/', views.twoopen, name='twoopen'),
]