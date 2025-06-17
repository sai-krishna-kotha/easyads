from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.create_ad, name='create_ad'),
    path('temp/', views.create_ad, name='create_ad'),
    path('', views.dashboard, name='dashboard'),
    
]
