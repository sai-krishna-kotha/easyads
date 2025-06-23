# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, HttpResponse
from .forms import UserSignUpForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import User
from django.contrib import messages  # for error messages
from django.contrib.auth import logout

def testing(request):
    return render(request, 'testing.html')

def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect('signin')  # Use the name of your signin URL
        else:
            # Add form errors to messages
            print(form.errors.items())
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
            return redirect('signup')  # Use the name of your signup URL
    else:
        form = UserSignUpForm()
    
    return render(request, 'app1_users/signup.html', {'form': form})


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
                # user_obj = User.objects.get(email=email)
                user = authenticate(request, email=email, password=password, user_type=user_type)
                if user is not None:
                    print(user.user_type)
                    login(request, user)
                    return redirect('home')  # change 'home' to your actual home url name
                else:
                    messages.error(request, "Invalid password.")
            except User.DoesNotExist:
                messages.error(request, "Email does not exist.")
        else:
            # If form is invalid, add form errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

        # After handling POST errors, redirect to GET signin page
        return redirect('signin')  # change 'signin' to your signin url name

    else:
        form = LoginForm()

    return render(request, 'app1_users/signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('signin')  # or 'signin' if you prefer


def home(request):
    return render(request, "home.html")

def reset_password(request):
    return render(request, "app1_users/reset-pass.html")

def filter_fields(request):
    pass
