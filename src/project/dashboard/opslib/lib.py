import openstack
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .objects import (
    object_images,
    object_flavors,
    object_networks
)

class opsbase(object):    
    conn = None
    def __init__(self):      
        self.conn = openstack.connect(
            auth_url='http://172.16.4.200:5000/v3/',
            project_name='admin',
            username='admin',
            password='Welcome123',
            region_name='RegionOne',
            user_domain_name='default',
            project_domain_name='default'
        )

# image service
    def image_list_images(self):
        print("List Images:")
        # list_images = []
        # for image in self.conn.image.images():
        #     list_images.append(image)
        return self.conn.image.images()
            
    def image_upload_image(self, name = 'imageSDK', path = '', disk_format = 'qcow2', container_format = 'bare', visibility = 'public'):
        print("Upload Image:")
        data_path_image = path
        name_image = name
        disk_format_image = disk_format
        container_format_image = container_format
        visibility_image = visibility        
        image_attrs = {
            'name': name,
            'data': default_storage.open(path, 'rb'),
            'disk_format': disk_format,
            'container_format': container_format,
            'visibility': visibility,
        }
        self.conn.image.upload_image(**image_attrs)

    def image_download_image(self, name = 'cirros', data_path = ''):
        print("Download Image:")
        name_image = name
        data_path_image = data_path
        os.path.join("", "abc")
        image = conn.image.find_image("cirros")
        with open(os.path.join("", name_image), "wb") as local_image:
            response = self.conn.image.download_image(image)
            local_image.write(response)

    def image_delete_image(self, name_id):
        print("Delete Image:")
        target_image = self.conn.image.find_image(name_id)
        self.conn.image.delete_image(target_image, ignore_missing=False)

    def image_find_image(self, name_id):
        image = self.conn.compute.find_image(name_id)
        return image
# network 
    def network_list_networks(self):
        print("List Networks:")                  
        return self.conn.network.networks()

# compute server
    def compute_create_vm(self, name_vm = '', name_image = 'cirros', name_flavor = 'm1.small', name_network = 'provider'):
        print("Create Server:")

        vm_name = name_vm
        vm_image = name_image
        vm_flavor = name_flavor
        vm_network = name_network

        image = self.conn.compute.find_image(vm_image)
        flavor = self.conn.compute.find_flavor(vm_flavor)
        network = self.conn.network.find_network(vm_network)

        server = self.conn.compute.create_server(
            name=vm_name, image_id=image.id, flavor_id=flavor.id,
            networks=[{"uuid": network.id}])

        server = self.conn.compute.wait_for_server(server)

    def compute_delete_server(self, name_id):
        print("Delete Server:")
        server = self.conn.compute.find_server(name_id)
        self.conn.compute.delete_server(server)

    def compute_list_servers(self):
        print("List Servers:")
        list_servers = []
        for server in self.conn.compute.servers():
            #print(server)
            name_image = self.image_find_image(server.image['id'])
            if name_image is None:
                server.image['name_image'] = 'Image has deleted'
            else:
                server.image['name_image'] = name_image.name
            
            name_flavor = self.compute_find_flavor(server.flavor['id'])
            if name_flavor is None:
                server.flavor['name_flavor'] = 'Flavor has deleted'
            else:
                server.flavor['name_flavor'] = name_flavor.name

            list_servers.append(server)
        return list_servers
    
    def compute_shutdown_server(self, name_id = ''):
        self.conn.compute.stop_server(name_id)

    def compute_startup_server(self, name_id = ''):
        self.conn.compute.start_server(name_id)
    
    def compute_get_console_server(self, name_id = ''):
        return self.conn.get_server_console(name_id)
# compute flavor
    def compute_list_flavors(self,):
        print("List Flavors:")
        return self.conn.compute.flavors()

    def compute_find_flavor(self, name_id):
        print("Find Flavor:")
        flavor = self.conn.compute.find_flavor(name_id)
        return flavor
    
    def compute_create_flavor(self, name , vcpu = '1', ram = '512', disk = '1'):
        print("Create flavor:")

        flavor_name = name
        flavor_vcpu = vcpu
        flavor_ram = ram
        flavor_disk = disk
      
        server = self.conn.compute.create_flavor(
            name = flavor_name, 
            vcpus = flavor_vcpu, 
            ram = flavor_ram, 
            disk = flavor_disk
        )

    def compute_delete_flavor(self, name_id):
        print("Delete Flavor:")
        flavor = self.conn.compute.delete_flavor(name_id)
        return flavor