from django.shortcuts import render

# Create your views here.

def login_view(request):        
    
    return render(request, 'authencation/login.html')

def registered_view(request):
    
    return render(request, 'authencation/registered.html')

def logout_view(request):
    
    return redirect('login_view')