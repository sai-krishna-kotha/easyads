"""
URL configuration for easyads project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
<<<<<<< HEAD
from accounts.views import signin
from classifieds.views import HomePageView,AboutView,ContactView
=======
from users.views import signin
from user_management.views import HomePageView,AboutView,ContactView
>>>>>>> 260fb9cf69e02f6c538eae5c14c1c6b8f96d97d5
from django.conf.urls.static import static
urlpatterns = [
    path('admin/login/', signin,name="signin"),
    path('admin/', admin.site.urls),
    path('',HomePageView.as_view(), name='home'),
    path('about/',AboutView.as_view(), name="about"),
    path('contact/',ContactView.as_view(), name="contact"),
<<<<<<< HEAD
    path('users/', include('accounts.urls')),
    path('ads/', include('classifieds.urls')),
=======
    path('users/', include('users.urls')),
    path('ads/', include('user_management.urls')),
>>>>>>> 260fb9cf69e02f6c538eae5c14c1c6b8f96d97d5
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)