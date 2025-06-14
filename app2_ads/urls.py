from django.urls import path
from .views import create_ad

urlpatterns = [
    path('post/', create_ad, name='create_ad'),
    path('', create_ad, name='create_ad'),
    
]
