from django import forms
from .models import Ad, Seller
from app1_users.models import User

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'location', 'image', 'category']
class SellerForm(forms.ModelForm):
    business_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Business Name'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter phone No.'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter Address','rows':4}))
    class Meta:
        model = Seller
        exclude = ['verified', 'user']
        # fields = ['business_name', 'phone', 'address']
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if any(char.isalpha() for char in phone):
            raise forms.ValidationError("Phone number should not contain letters.")
        return phone