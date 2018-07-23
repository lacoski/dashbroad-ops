from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('image_upload/', views.image_upload, name='image_upload'),
    path('network_list/', views.network_list, name='network_list'),
    # Server 
    path('server_list/', views.server_list, name='server_list'),
    path('server_shutdown/', views.server_shutdown, name='server_shutdown'),
    path('server_shutdown/<slug:key>', views.server_shutdown, name='server_shutdown_id'),
    path('server_shutdown/<slug:key>/<slug:name>', views.server_shutdown, name='server_shutdown_name'),

    path('server_startup/', views.server_startup, name='server_startup'),
    path('server_startup/<slug:key>', views.server_startup, name='server_startup_id'),
    path('server_startup/<slug:key>/<slug:name>', views.server_startup, name='server_startup_name'),

    path('server_get_console/', views.server_get_console, name='server_get_console'),
    path('server_get_console/<slug:key>', views.server_get_console, name='server_get_console_id'),
    path('server_get_console/<slug:key>/<slug:name>', views.server_get_console, name='server_get_console_name'),

    path('server_delete/', views.server_delete, name='server_delete'),
    path('server_delete/<slug:key>', views.server_delete, name='server_delete_id'),
    path('server_delete/<slug:key>/<slug:name>', views.server_delete, name='server_delete_name'),

    path('server_create/', views.server_create, name='server_create'),  
    # flavor
    path('flavor_list/', views.flavor_list, name='flavor_list'),
    path('flavor_create/', views.flavor_create, name='flavor_create'),

    path('flavor_delete/', views.flavor_delete, name='flavor_delete'),
    # path('flavor_delete/<slug:key>', views.flavor_delete, name='flavor_delete_id'),
    #re_path(r'^flavor_delete/(?P<key>[\w-]+)', views.flavor_delete, name='flavor_delete_name'),
    re_path(r'^flavor_delete/(?P<key>[\w-]+)/(?P<name>[\w.]+)', views.flavor_delete, name='flavor_delete_name'),

    # image 
    path('image_list/', views.image_list, name='image_list'),
    path('image_upload/', views.image_upload, name='image_upload'),
    path('image_delete/', views.image_delete, name='image_delete'),
    path('image_delete/<slug:key>', views.image_delete, name='image_delete_id'),
    path('image_delete/<slug:key>/<slug:name>', views.image_delete, name='image_delete_name'),

]
