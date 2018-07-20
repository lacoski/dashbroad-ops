from lib import opsbase

def main():
    api = opsbase()
    list_test = api.image_list_images()
    
    print(type(list_test))
    for obj in list_test:
        obj.show_image()
    #api.create_vm('demolib')  
    #api.delete_server('demolib')

if __name__ == '__main__':
    main()  