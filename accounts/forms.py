from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserSignUpForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        ('', '----------'),
        ('customer', 'Customer'),
        ('seller', 'Seller'),
    )
    first_name = forms.CharField(max_length=150, required=True, label='First Name',widget=forms.TextInput(attrs={'class': 'form-control form-control-sm py-1', 'placeholder': 'Full Name', 'autofocus': True}))
    
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm py-1', 'placeholder': 'Email'}))
    
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True, label='Sign up as',widget=forms.Select(attrs={'class': 'form-select form-select-sm py-1'}))

    class Meta:
        model = User
        fields = ( 'first_name', 'email', 'user_type', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control form-control-sm py-1', 'placeholder': 'Password','id':'password-input'})
        
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-sm py-1', 'placeholder': 'Confirm Password','id':'password-input'})
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = self.cleaned_data['user_type']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', required=True ,widget=forms.EmailInput(attrs={'id':'email-field', 'class':'form-control form-control-sm py-1', 'placeholder':'Email','autofocus': True}))
    
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'id':'password-input', 'class':'form-control form-control-sm py-1', 'placeholder':'Password'}))
    
    user_type = forms.ChoiceField(
        choices=[('', '----------'),('customer', 'Customer'), ('seller', 'Seller'), ('admin', 'Admin')],
        label='Login as',
        widget= forms.Select(attrs={'id':'user-type-field', 'class':'form-select form-select-sm py-1'})
    )
