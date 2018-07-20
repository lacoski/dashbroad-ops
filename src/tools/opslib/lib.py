import openstack
import os
from objects import object_images


def create_connection(auth_url, region, project_name, username, password):
    return openstack.connect(
        auth_url=auth_url,
        project_name=project_name,
        username=username,
        password=password,
        region_name=region,
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

# image function            
    def image_list_images(self):
        print("List Images:")
        list_images = []
        for image in self.conn.image.images():
            temp_obj = object_images(
                s_Name = image.name,
                s_Status = image.status,
                s_Visibility = image.visibility,
                s_Disk_Format = image.disk_format,
                s_Size = image.size,
            )
            #print(image)
            list_images.append(temp_obj)
        return list_images
            

    def image_upload_image(self, name = 'imageSDK', path = '', disk_format = 'qcow2', container_format = 'bare', visibility = 'public'):
        print("Upload Image:")
        data_path_image = path
        name_image = name
        disk_format_image = disk_format
        container_format_image = container_format
        visibility_image = visibility
        image_attrs = {
            'name': 'imageSDKup',
            'data': open('cirros.qcow2', 'rb'),
            'disk_format': 'qcow2',
            'container_format': 'bare',
            'visibility': 'public',
        }
        self.conn.image.upload_image(**image_attrs)

    def image_download_image(self, name = 'cirros', data_path = ''):
        print("Download Image:")
        name_image = name
        data_path_image = data_path
        os.path.join("", "abc")
        image = self.conn.image.find_image("cirros")
        with open(os.path.join("", name_image), "wb") as local_image:
            response = self.conn.image.download_image(image)
            local_image.write(response)

    def image_delete_image(self, name):
        print("Delete Image:")
        name_image = name 
        target_image = self.conn.image.find_image(name_image)
        self.conn.image.delete_image(target_image, ignore_missing=False)

    def network_list_networks(self):
        print("List Networks:")
        for network in self.conn.network.networks():
            print(network)
            print(network.id)


    def compute_list_servers(self):
        print("List Servers:")
        for server in self.conn.compute.servers():
            print(server)

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

    def compute_delete_server(self, name):
        print("Delete Server:")
        name_server = name
        server = self.conn.compute.find_server(name_server)
        print(server)
        self.conn.compute.delete_server(server)

    def compute_list_flavors(self,):
        print("List Flavors:")
        list_flavors = []
        for flavor in self.conn.compute.flavors():
            list_flavors.append(flavor)

        return list_flavors