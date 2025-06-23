from django import forms
from .models import Ad, Seller
from app1_users.models import User

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'location', 'image', 'category']
class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['business_name', 'phone', 'address']
    