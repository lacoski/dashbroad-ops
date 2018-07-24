from django.urls import path, re_path

from . import views

urlpatterns = [    
    path('login/', views.login_view, name = 'login_view'),
    path('registered/', views.registered_view, name = 'registered_view'),
    path('logout/', views.logout_view , name = 'logout_view'),    
]
