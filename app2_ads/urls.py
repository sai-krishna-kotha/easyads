from django.urls import path
from .views import (
    AdCreateView,
    SellerDashboardView,
    SellerRegistrationView,
    AdUpdateView,
    AdDeleteView,
    AdDetailView,
    SellerProfileView,
    CustomerDashboardView,
    CustomerProfileView,
    AddToWishlist,
    RemoveFromWishlist,
)

app_name = 'app2_ads'

urlpatterns = [
    path('post-ad/', AdCreateView.as_view(), name='create_ad'),
    path('seller-dashboard/', SellerDashboardView.as_view(), name='seller_dashboard'),
    path('seller-register/', SellerRegistrationView.as_view(), name='seller_registration'),
    path('<int:pk>/edit/', AdUpdateView.as_view(), name='edit_ad'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name='delete_ad'),
    path('<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('seller_profile/<int:pk>/',SellerProfileView.as_view() ,name='seller_profile'),
    path('customer_dashboard/',CustomerDashboardView.as_view(), name='customer_dashboard'),
    path('customer_profile/',CustomerProfileView.as_view(), name='customer_profile'),
    path('add_it/<int:pk>', AddToWishlist.as_view(), name="add_to_wishlist"),
    path('remove_it/<int:pk>', RemoveFromWishlist.as_view(), name="remove_from_wishlist"),
]
