from django.shortcuts import render, redirect
from django.contrib.auth import (
    login,
    logout,
    authenticate
)
from .objects import User as auth_user
from .objects import set_session_from_user
from django.core import exceptions 
from django.utils import functional
from .forms import LoginForm
from django.contrib.auth import views as django_auth_views


from .forms import (
    LoginForm
)

# Create your views here.

def login_view(request):        
    if request.user.is_authenticated:
        return redirect("/")
    
    print(request.session.get('token','none'))
    print(request.session.get('user_id','none'))
    print(request.session.get('project_id','none'))
    print(request.session.get('project_name','none'))
    print(request.session.get('project_domain_name','none'))

    print(request.user.is_authenticated)
    print(type(request.user.is_authenticated))


    
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user_auth = authenticate(username=username, password=password)
        print('------- View login')
        print(type(user_auth))
        # print(user_auth.token)
        # print(user_auth.id)
        # print(user_auth.project_id)
        # print(user_auth.project_name)
        # print(user_auth.project_domain_name)

        if user_auth:
            print('Login session')
            print(type(user_auth))

            #check = login(request, user_auth)
            django_auth_views.login(
                request, 
                template_name='authencation/login.html',
                authentication_form=form
            )
            print('Set session')
            set_session_from_user(request, user_auth)            
            
        print('------- out View login')
        return redirect("server_list")        
    return render(request, 'authencation/login.html')

def registered_view(request):    
    return render(request, 'authencation/registered.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')