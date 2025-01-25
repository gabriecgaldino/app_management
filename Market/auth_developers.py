from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class DeveloperAuthBackend(ModelBackend):
    """
    Custom authentication backend to validate users specifically
    for the Developer Central.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            # Verifique se o usuário é válido para a central do desenvolvedor
            if user.is_developer and user.check_password(password):
                print('desenvolvedor')
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id, is_developer=True)
        except User.DoesNotExist:
            return None