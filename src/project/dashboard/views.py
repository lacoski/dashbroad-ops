from django.shortcuts import render
from django.http import HttpResponse
from .opslib.lib import opsbase

# Create your views here.

api_ops = opsbase()

def index(request):
    list_object = api_ops.image_list_images()
    return render(request, 'dashboard/index.html', {'images' : list_object})

def image_list(request):
    list_object = api_ops.image_list_images()
    return render(request, 'dashboard/image_list.html', {'images' : list_object})

def image_upload(request):
    return render(request, 'dashboard/image_upload.html')

def server_list(request):
    return render(request, 'dashboard/server_list.html')