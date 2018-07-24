from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os

from django.http import HttpResponse
from .opslib.lib import opsbase
from dashboard.forms import (
    StateServerForm,
    CreateServerForm,
    CreateFlavorForm,
    StateFlavorForm,
    CreateImageForm,
    StateImageForm
)

# Create your views here.

api_ops = opsbase()

# image

FORMAT_IMAGE=[    
    'qcow2',
    'raw',
]
def index(request):
    list_object = api_ops.image_list_images()
    request.session['test'] = 'session from test'
    return redirect('server_list')

def image_list(request):
    list_object = api_ops.image_list_images()
    return render(request, 'dashboard/image_list.html', {'images' : list_object})

def image_upload(request):
    list_format = FORMAT_IMAGE
    form = CreateImageForm(request.POST or None)
    # if request.method == 'POST':
    #     print(request.FILES['uploadFromPC'])
    if form.is_valid() and request.FILES['uploadFromPC']:
        key = form.cleaned_data['name']
        disk_format = form.cleaned_data['disk_format']
        file_image = request.FILES['uploadFromPC']
        # print(request.FILES['uploadFromPC'])
        # print(type(request.FILES['uploadFromPC']))        
        path_file = os.path.join(settings.PATH_CACHE, file_image.name)
        #print(path_file)
        path_save = default_storage.save(path_file, ContentFile(file_image.read()))
        #print(path)        
        api_ops.image_upload_image(
            name = key, 
            path = path_save, 
            disk_format = 'qcow2'
        )
        messages.add_message(request, messages.INFO, 'Tạo động thành công, đợi 5-10s để hệ thống cập nhật trạng thái')
        return redirect('image_list')
    print(form.errors)
    return render(request, 'dashboard/image/upload.html', {'formats':list_format})

def image_delete(request, key = '', name = ''):
    if request.method == "POST":
        form = StateImageForm(request.POST or None)
        if form.is_valid():
            key_id = form.cleaned_data['key']
            print(key_id)
            api_ops.image_delete_image(
                name_id = key_id
            )
            messages.add_message(request, messages.INFO, 'Xóa thành công, đợi 5-10s để hệ thống cập nhật trạng thái')
            return redirect('image_list')
        return render(request, 'dashboard/image/delete.html')
    return render(request, 'dashboard/image/delete.html', {'id':key, 'name': name})
# flavor
def flavor_list(request):
    list_object = api_ops.compute_list_flavors
    return render(request, 'dashboard/flavor_list.html', {'flavors' : list_object})

def flavor_delete(request, key = '', name = ''):
    if request.method == "POST":
        form = StateFlavorForm(request.POST or None)
        if form.is_valid():
            key_id = form.cleaned_data['key']
            print(key_id)
            api_ops.compute_delete_flavor(key_id)
            messages.add_message(request, messages.INFO, 'Xóa thành công, đợi 5-10s để hệ thống cập nhật trạng thái')
            return redirect('flavor_list')
        return render(request, 'dashboard/flavor/delete.html')
    return render(request, 'dashboard/flavor/delete.html', {'id':key, 'name': name})

def flavor_create(request):
    if request.method == "POST":
        form = CreateFlavorForm(request.POST or None)
        if form.is_valid():
            key = form.cleaned_data['name']
            vcpus = form.cleaned_data['vcpus']
            ram = form.cleaned_data['ram']
            disk = form.cleaned_data['disk']
            
            api_ops.compute_create_flavor(
                name = key, 
                vcpu = vcpus, 
                ram = ram, 
                disk = disk
            )
            messages.add_message(request, messages.INFO, 'Tạo động thành công, đợi 5-10s để hệ thống cập nhật trạng thái')
            return redirect('flavor_list')
        return render(request, 'dashboard/flavor/create.html')

    return render(request, 'dashboard/flavor/create.html')

# network
def network_list(request):
    list_object = api_ops.network_list_networks
    return render(request, 'dashboard/network_list.html', {'networks' : list_object}) 

# vm
def server_list(request, ):
    list_object = api_ops.compute_list_servers
    #notification = request.POST.get('notification','')
    #notification = 'abs'
    if request.session.get('test'):
        print(request.session['test'])

    
    return render(request, 'dashboard/server_list.html', {'servers' : list_object}) 

def server_shutdown(request, key = '', name = ''):
    if request.method == "POST":
        form = StateServerForm(request.POST or None)
        if form.is_valid():
            key_id = form.cleaned_data['key']
            print(key_id)
            api_ops.compute_shutdown_server(key_id)
            
            messages.add_message(request, messages.INFO, 'Tắt thành công, đợi 5-10s để hệ thống cập nhật trạng thái')
            return redirect('server_list')
        return render(request, 'dashboard/server/shutdown.html')
    return render(request, 'dashboard/server/shutdown.html', {'id':key, 'name': name})

def server_startup(request, key = '', name = ''):
    if request.method == "POST":
        form = StateServerForm(request.POST or None)
        if form.is_valid():
            key_id = form.cleaned_data['key']
            api_ops.compute_startup_server(key_id)
            messages.add_message(request, messages.INFO, 'Khởi động thành công, đợi 5-10s để hệ thống cập nhật trạng thái')
            return redirect('server_list')
        return render(request, 'dashboard/server/startup.html')
    return render(request, 'dashboard/server/startup.html', {'id':key, 'name': name})

def server_get_console(request, key = '', name = ''):  
    server_console = api_ops.compute_get_console_server(key)
    return render(request, 'dashboard/server/get_console.html', {'id':key, 'name': name, 'server_console': server_console})

def server_delete(request, key = '', name = ''):
    if request.method == "POST":
        form = StateServerForm(request.POST or None)
        if form.is_valid():
            key_id = form.cleaned_data['key']
            #print(key_id)
            api_ops.compute_delete_server(key_id)
            messages.add_message(request, messages.INFO, 'Xóa thành công, đợi 5-10s để hệ thống cập nhật trạng thái')
            return redirect('server_list')
        return render(request, 'dashboard/server/delete.html')
    return render(request, 'dashboard/server/delete.html', {'id':key, 'name': name})

def server_create(request, key = '', name = ''):
    if request.method == "POST":
        form = CreateServerForm(request.POST or None)
        if form.is_valid():
            key_id = form.cleaned_data['name']
            flavor_id = form.cleaned_data['flavor_id']
            image_id = form.cleaned_data['image_id']
            network_id = form.cleaned_data['network_id']

            api_ops.compute_create_vm(
                name_vm = key_id, 
                name_image = image_id, 
                name_flavor = flavor_id, 
                name_network = network_id
            )
            messages.add_message(request, messages.INFO, 'Tạo động thành công, đợi 5-10s để hệ thống cập nhật trạng thái')
            return redirect('server_list')
        return render(request, 'dashboard/server/create.html')

    list_image = api_ops.image_list_images()
    list_flavor = api_ops.compute_list_flavors
    list_network = api_ops.network_list_networks

    return render(request, 'dashboard/server/create.html', {'images': list_image, 'flavors': list_flavor, 'networks': list_network})