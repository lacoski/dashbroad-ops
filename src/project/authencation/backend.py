from django.conf import settings
from django.contrib.auth.models import User
from .objects import User as auth_user
from authencation.objects import (
    Auth_Password,
    Token
)
from django.core import exceptions 

class NoPasswordBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            
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
            user = None
            print(username)
            print(password)
            passwd = Auth_Password(
                auth_url = 'http://172.16.4.200:5000/v3/', 
                region_site = 'RegionOne',         
                project_domain_name = 'default', 
                project_id = '91e4db1098934a3e9cc7babf97edf007', 
                project_name = 'admin',
                user_name = username, 
                user_password = password,
                user_domain_name = 'default'
            )   
            token_generate = Token(auth_ref = passwd)
            if token_generate.is_authenticated():
                user = auth_user(token_generate)  
                return user
            else:
                raise User.DoesNotExist
        
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
