from django.shortcuts import render
from django.http import HttpResponse
from .opslib.lib import opsbase

# Create your views here.

api_ops = opsbase()

# image
def index(request):
    list_object = api_ops.image_list_images()
    return render(request, 'dashboard/index.html', {'images' : list_object})

def image_list(request):
    list_object = api_ops.image_list_images()
    return render(request, 'dashboard/image_list.html', {'images' : list_object})

def image_upload(request):
    return render(request, 'dashboard/image_upload.html')

# flavor
def flavor_list(request):
    list_object = api_ops.compute_list_flavors
    return render(request, 'dashboard/flavor_list.html', {'flavors' : list_object})

# network
def network_list(request):
    list_object = api_ops.network_list_networks
    return render(request, 'dashboard/network_list.html', {'networks' : list_object}) 

# vm
def server_list(request):
    list_object = api_ops.compute_list_servers
    return render(request, 'dashboard/server_list.html', {'servers' : list_object}) 

def server_shutdown(request):
    return render(request, 'dashboard/server/shutdown.html') 
