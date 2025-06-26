from django.urls import path
from .views import (
    AdCreateView,
    SellerDashboardView,
    SellerRegistrationView,
    AdUpdateView,
    AdDeleteView,
    AdDetailView,
    SellerProfileView
)

app_name = 'app2_ads'

urlpatterns = [
    path('post-ad/', AdCreateView.as_view(), name='create_ad'),
    path('seller-dashboard/', SellerDashboardView.as_view(), name='seller_dashboard'),
    path('seller-register/', SellerRegistrationView.as_view(), name='seller_registration'),
    path('<int:pk>/edit/', AdUpdateView.as_view(), name='edit_ad'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name='delete_ad'),
    path('ads/<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('seller_profile/<int:pk>/',SellerProfileView.as_view() ,name='seller_profile'),

]
