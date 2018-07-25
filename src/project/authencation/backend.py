from django.conf import settings
# from django.contrib.auth.models import User
from authencation import user.User as auth_user


class NoPasswordBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            if user:
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class KeystoneBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            if user:
                return user
        except User.DoesNotExist:
            return None
            
    def get_user(self, user_id): 
        if (hasattr(self, 'request') and
                user_id == self.request.session["user_id"]):
            token = self.request.session['token']

            user = auth_user.create_user_from_token(self.request, token, endpoint, services_region)
            return user
        else:
            return None
