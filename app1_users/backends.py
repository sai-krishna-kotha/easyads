from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailUserTypeBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, user_type=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            if user.user_type != user_type:
                return None
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
