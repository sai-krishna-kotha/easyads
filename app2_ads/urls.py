from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.create_ad, name='create_ad'),
    path('temp/', views.create_ad, name='create_ad'),
    path('/seller-dashboard', views.seller_dashboard, name='seller_dashboard'),
    path('/seller-registration',views.seller_registration, name="seller_registration"), 
]
