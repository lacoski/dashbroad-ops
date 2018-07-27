from django.shortcuts import render, redirect
from django.contrib.auth import (
    login,
    logout,
    authenticate
)
from .objects import User as auth_user
from .objects import (
    set_session_from_user,
    create_session_from_token
)

from django.core import exceptions 
from django.utils import functional
from .forms import LoginForm
from django.contrib.auth import views as django_auth_views


from .forms import (
    LoginForm
)

# Create your views here.

def login_view(request):        
    if request.session.get('token','none') != 'none':
        return redirect("server_list")
    
    # print(request.session.get('token','none'))
    # print(request.session.get('user_id','none'))
    # print(request.session.get('project_id','none'))
    # print(request.session.get('project_name','none'))
    # print(request.session.get('project_domain_name','none'))
    
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user_auth = authenticate(username=username, password=password)        
        if user_auth:
            print('Create session')
            set_session_from_user(request, user_auth)            
                    
        return redirect("server_list")        
    return render(request, 'authencation/login.html')

def registered_view(request):    
    return render(request, 'authencation/registered.html')

def logout_view(request):
    print(request.session.keys())    
    request.session.clear()      
    return redirect('login_view')