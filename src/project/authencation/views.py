from django.shortcuts import render
from django.contrib import auth
from .objects import User as auth_user
from .objects import set_session_from_user

from .forms import (
    LoginForm
)

# Create your views here.

def login_view(request):        
    if request.user.is_authenticated:
        return redirect("/")
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')

        request.user = auth.authenticate(username=username, password=password)
        set_session_from_user(request, request.user)
        auth.login(request, request.user)
     
        if next:
            return redirect(next)
        return redirect("server_list")
    return render(request, 'authencation/login.html')

def registered_view(request):
    
    return render(request, 'authencation/registered.html')

def logout_view(request):
    auth.logout(request)
    return redirect('login_view')