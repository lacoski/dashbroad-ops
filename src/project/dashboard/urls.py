from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('image_list/', views.image_list, name='image_list'),
    path('image_upload/', views.image_upload, name='image_upload'),
    path('flavor_list/', views.flavor_list, name='flavor_list'),
    path('network_list/', views.network_list, name='network_list'),
    path('server_list/', views.server_list, name='server_list'),
]
