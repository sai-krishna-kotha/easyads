from django import forms
from .models import Ad, Seller
from app1_users.models import User

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'location','category']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Enter Ad Title'}),
            'description': forms.Textarea(attrs={'placeholder':'Enter Ad Description','rows':4}),
            'price': forms.NumberInput(attrs={'placeholder':'Enter Ad price','step':'0.1'}),
            'location': forms.TextInput(attrs={'placeholder':'Enter your city'})
        }
class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        exclude = ['verified', 'user']
        # fields = ['business_name', 'phone', 'address']
        widgets = {
            'business_name': forms.TextInput(attrs={'placeholder':'Enter Business Name'}),
            'phone': forms.TextInput(attrs={'placeholder':'Enter phone No.'}),
            'address': forms.TextInput(attrs={'placeholder':'Enter Address','rows':4})
        }
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if any(char.isalpha() for char in phone):
            raise forms.ValidationError("Phone number should not contain letters.")
        return phone