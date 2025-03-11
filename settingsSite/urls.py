from django.urls import path
from . import views

urlpatterns = [
    path('', views.settings, name='settings'),
    path('developer/', views.developer, name='developer'),
    path('partners/', views.partners, name='partners'),
    path('partners/fiz_face', views.fiz_face, name='fiz_face'),
    path('partners/legal_face', views.legal_face, name='legal_face'),
]