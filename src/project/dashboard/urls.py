from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('image_list/', views.image_list, name='image_list'),
    path('image_upload/', views.image_upload, name='image_upload'),
]
