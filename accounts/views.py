from django.shortcuts import render, redirect, HttpResponse
from .forms import UserSignUpForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import User
from django.contrib import messages  # for error messages
from django.contrib.auth import logout
from classifieds.models import Customer

def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully. You can now log in.")
            if form.cleaned_data['user_type'] == 'customer':
                Customer.objects.create(user=user)
            return redirect('accounts:signin') 
        else:
            print(form.errors.items())
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
            return redirect('accounts:signup') 
    else:
        form = UserSignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']
            print(form.cleaned_data)
            try:
                user = authenticate(request, email=email, password=password, user_type=user_type)
                if user is not None:
                    print(user.user_type)
                    login(request, user)
                    return redirect('home')  
                else:
                    messages.error(request, "Invalid password.")
            except User.DoesNotExist:
                messages.error(request, "Email does not exist.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

        return redirect('accounts:signin') 
    else:
        form = LoginForm()

    return render(request, 'accounts/signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('accounts:signin')


def reset_password(request):
    return render(request, "accounts/reset_password.html")


def health(request):
    return HttpResponse('Everything is fine. Probably...😎',status=200)