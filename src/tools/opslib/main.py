from lib import opsbase
from openstack.compute.v2.flavor import Flavor


def main():
    api = opsbase()
    # list_test = api.image_list_images()
    # api.network_list_networks()
    # print(type(list_test))
    # for obj in list_test:
    #     obj.show_image()
    #api.create_vm('demolib')  
    #api.delete_server('demolib')
    test = api.compute_shutdown_server()
        
if __name__ == '__main__':
    main()  