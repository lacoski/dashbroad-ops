from django.contrib.auth import models
from django.db import models as db_models
from django.conf import settings
from abc import ABC, abstractmethod
from keystoneauth1.identity import v3
from keystoneclient.v3 import client
from keystoneauth1 import session
from keystoneauth1.exceptions.http import Unauthorized

from openstack import connection

def set_session_from_user(request, user):
    request.session['token'] = user.token
    request.session['user_id'] = user.id
    request.session['project_id'] = user.project_id
    request.session['project_name'] = user.project_name
    request.session['project_domain_name'] = user.project_domain_name
    # Update the user object cached in the request
    request._cached_user = user
    request.user = user

class Auth_Base(ABC):
    auth_url = ''
    region_site = ''
    project_domain_id = ''
    project_domain_name = ''
    project_id = ''
    project_name = ''

    def __init__(self, auth_url = None, region_site = None, project_domain_id = None, 
                project_domain_name = None, project_id = None, project_name = None):
        self.auth_url = auth_url
        self.region_site = region_site
        self.project_domain_id = project_domain_id
        self.project_domain_name = project_domain_name
        self.project_id = project_id
        self.project_name = project_name

    @abstractmethod
    def authenticate_type(self):             
        raise NotImplementedError("Subclass must implement abstract method")

    def __str__(self):
        return self.auth_url + " " + self.region_site + " " + self.project_domain_id + " " + self.project_domain_name + \
                     " " + self.project_id + " " + self.project_name

class Auth_Password(Auth_Base):   
    user_name = ''
    user_password = ''
    user_domain_name = ''
    def __init__(self, auth_url = None, region_site = None, project_domain_id = None, 
                    project_domain_name = None, project_id = None, project_name = None, 
                    user_name = None, user_password = None, user_domain_name = None):
        super().__init__(auth_url, region_site, project_domain_id, project_domain_name, project_id, project_name)
        self.user_name = user_name
        self.user_password = user_password
        self.user_domain_name = user_domain_name

    def __str__(self):
        return super().__str__() + " " + self.user_name + " " + self.user_password

    def authenticate_type(self):             
        return 'Password'

class Auth_Token(Auth_Base):   
    token_string = ''

    def __init__(self, auth_url = None, region_site = None, project_domain_id = None, 
                    project_domain_name = None, project_id = None, project_name = None, 
                    token_string = None):
        super().__init__(auth_url, region_site, project_domain_id, project_domain_name, project_id, project_name)
        self.token_string = token_string

    def __str__(self):
        return super().__str__() + " " + self.token_string
    
    def authenticate_type(self):             
        return 'Token'

class Token(object):
    session_auth = None

    def __init__(self, auth_ref = None):
        """
        auth_ref = Lớp chung cho cả Auth_Password và Auth_Token. Sử dụng tính chất đa hình Python OOP 
        """
        self.auth_url = auth_ref.auth_url
        self.region_site = auth_ref.region_site
        self.project_domain_id = auth_ref.project_domain_id
        self.project_domain_name = auth_ref.project_domain_name
        self.project_id = auth_ref.project_id
        self.project_name = auth_ref.project_name
        if auth_ref.authenticate_type() == 'Token':            
            self.session_auth = v3.Token(
                auth_url=self.auth_url,
                token=auth_ref.token_string,
                project_id=self.project_id,
                project_name=self.project_name,
                project_domain_name=self.project_domain_name,                
            )
        elif auth_ref.authenticate_type() == 'Password':
            self.session_auth = v3.Password(
                auth_url=self.auth_url,
                username=auth_ref.user_name,
                password=auth_ref.user_password,
                project_id=self.project_id,
                project_name=self.project_name,
                project_domain_name=self.project_domain_name,
                user_domain_name=auth_ref.user_domain_name
            )

    def get_token(self):
        sess = session.Session(auth=self.session_auth)
        token = sess.get_auth_headers()
        return token['X-Auth-Token']

    def is_authenticated(self):
        sess = session.Session(auth=self.session_auth)
        try:
            resp = sess.get('http://172.16.4.200:5000/v3/', authenticated=True)
            return True
        except Unauthorized:
            return False

    def get_identity(self):
        """
        Trả về lớp keystoneclient.access.AccessInfoV3
        """
        sess = session.Session(auth=self.session_auth)
        keystone = client.Client(session=sess)        
        return keystone.get_raw_token_from_identity_service(
            auth_url='http://172.16.4.200:5000/v3/',
            token = self.get_token()
        )

class User(models.AbstractBaseUser, models.AnonymousUser):
    keystone_user_id = db_models.CharField(primary_key=True, max_length=255)
    USERNAME_FIELD = 'keystone_user_id'

    def __init__(self, token=None):
        
        data_identity = token.get_identity()
        self.id = data_identity.user_id
        self.pk = data_identity.user_id
        self.token = token
        self.keystone_user_id = data_identity.user_id
        self.username = data_identity.username
        self.domain_id = data_identity.user_domain_id
        self.domain_name = data_identity.user_domain_name
        self.project_id = token.project_id
        self.project_name = token.project_name
        self.project_domain_id = token.project_domain_id
        self.project_domain_name = token.project_domain_name
        self.password_expires_at = data_identity.expires

    def __unicode__(self):
        return self.username

    def is_token_expired(self):
        return False 

    @property
    def is_authenticated(self):
        # if (self.token is not None and utils.is_token_valid(self.token)):
        #     return True
        # else:
        #     return False
        return True
    
    @property
    def is_anonymous(self):
        return not self.is_authenticated

    @property
    def is_active(self):
        return True

    @property
    def is_superuser(self):
        return True 

    def save(*args, **kwargs):
        # Presume we can't write to Keystone.
        pass

    def delete(*args, **kwargs):
        # Presume we can't write to Keystone.
        pass


# def create_user_from_token(request, token)
#     pass