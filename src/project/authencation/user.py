from django.contrib.auth import models
from django.db import models as db_models
from django.conf import settings

def create_user_from_token(request, token)
    return User()

class Auth_Base(object):
    auth_url = ''
    region_site = ''

    domain_id = ''
    domain_name = ''

    project_id = ''
    project_name = ''

    def __init__(self):
        pass

class Auth_Password(Auth_Base):   
    user_name = ''
    user_password = ''

    def __init__(self):
        pass

class Auth_Token(Auth_Base):   
    token_string = ''

    def __init__(self):
        pass


class Token(object):
    def __init__(self, auth_password = None, auth_token = None):
        self.user = user
        self.user_domain_id = auth_ref.user_domain_id
        self.user_domain_name = auth_ref.user_domain_name 
        self.id = auth_ref.auth_token
        self.unscoped_token = unscoped_token
        self.project = project
        self.tenant = self.project
        self.is_federated = auth_ref.is_federated
        self.roles = [{'name': role} for role in auth_ref.role_names]
        self.serviceCatalog = auth_ref.service_catalog.catalog

class User(models.AbstractBaseUser, models.AnonymousUser):
    keystone_user_id = db_models.CharField(primary_key=True, max_length=255)
    USERNAME_FIELD = 'keystone_user_id'

    def __init__(self, id=None, token=None, user=None, domain_id=None, domain_name=None,
                project_id=None, project_name=None, unscoped_token=None, 
                password=None, password_expires_at=None):
        self.id = id
        self.pk = id
        self.token = token
        self.keystone_user_id = id
        self.username = user
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.project_id = project_id
        self.project_name = project_name
        self.unscoped_token = unscoped_token
        # Required by AbstractBaseUser
        self.password = None
        self.password_expires_at = password_expires_at

    def __unicode__(self):
        return self.username

    def is_token_expired(self):
        pass 

    def is_authenticated(self):
        # if (self.token is not None and utils.is_token_valid(self.token)):
        #     return True
        # else:
        #     return False
        return True
    
    def is_anonymous(self):
        return not self.is_authenticated

    def is_active(self):
        return True

    def is_superuser(self):
        return True 

    def save(*args, **kwargs):
        # Presume we can't write to Keystone.
        pass

    def delete(*args, **kwargs):
        # Presume we can't write to Keystone.
        pass
