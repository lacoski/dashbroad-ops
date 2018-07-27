from django.conf import settings
from django.contrib.auth.models import User
from .objects import User as auth_user
from authencation.objects import (
    Auth_Password,
    Auth_Token,
    Token,
    create_user_from_token
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
        #try:            
        print("----------- In backend")

        print(username)
        print(password)
        passwd = Auth_Password(
            auth_url = settings.AUTH_URL, 
            region_site = settings.REGION_SITE,         
            project_domain_name = settings.PROJECT_DOMAIN_NAME, 
            project_id = settings.PROJECT_ID, 
            project_name = settings.PROJECT_NAME,
            user_name = username, 
            user_password = password,
            user_domain_name = 'default'
        )   
        token_generate = Token(auth_ref = passwd)
        check_auth_token = token_generate.is_authenticated()

        if check_auth_token:
            print(token_generate.get_identity())
            user = auth_user(
                id = token_generate.get_identity().user_id, 
                token = token_generate.get_token(),                     
                username = token_generate.get_identity().username, 
                domain_id = token_generate.get_identity().user_domain_id, 
                domain_name = token_generate.get_identity().user_domain_name, 
                project_id = token_generate.project_id, 
                project_name = token_generate.project_name,  
                project_domain_id = token_generate.project_domain_id, 
                project_domain_name = token_generate.project_domain_name, 
                password_expires_at = token_generate.get_identity().expires
            )              
            return user
        else:
            return None
    
        # except:
        #     return None
            
    def get_user(self, user_id): 
        if (hasattr(self, 'request') and
                user_id == self.request.session["user_id"]):
            token = self.request.session['token']            

            user = create_user_from_token(self.request, token)
            return user
        else:
            return None
