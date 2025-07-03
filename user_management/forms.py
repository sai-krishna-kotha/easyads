from django import forms
from .models import Ad, Seller,City
from users.models import User

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'city','category']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Enter Ad Title'}),
            'description': forms.Textarea(attrs={'placeholder':'Enter Ad Description','rows':4}),
            'price': forms.NumberInput(attrs={'placeholder':'Enter Ad price','step':'0.1'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.all().order_by('name')


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        exclude = ['verified', 'user']
        # fields = ['business_name', 'phone', 'city']
        widgets = {
            'business_name': forms.TextInput(attrs={'placeholder':'Enter Business Name'}),
            'phone': forms.TextInput(attrs={'placeholder':'Enter phone No.'}),
            'city': forms.TextInput(attrs={'placeholder':'Enter city'})
        }
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if any(char.isalpha() for char in phone):
            raise forms.ValidationError("Phone number should not contain letters.")
        return phone
 
class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Your Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Your Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    subject = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )