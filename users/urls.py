from django.urls import path
from . import views

<<<<<<<< HEAD:accounts/urls.py
app_name = 'accounts'
========
app_name = 'users'
>>>>>>>> 260fb9cf69e02f6c538eae5c14c1c6b8f96d97d5:users/urls.py


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('reset-pass/', views.reset_password, name='reset_password'),
]
