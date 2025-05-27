from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    username = None  # remove username field
    email = models.EmailField(_('email address'), unique=True)
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    USERNAME_FIELD = 'email'       # make email the unique identifier
    REQUIRED_FIELDS = []           # email & password required by default; no extra fields required

    def __str__(self):
        return self.email
