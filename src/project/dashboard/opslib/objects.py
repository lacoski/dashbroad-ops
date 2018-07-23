class object_images(object):
    Name = ''
    Type = ''
    Status = ''
    Visibility = ''
    Disk_Format	= ''
    Size = ''
    def __init__(
        self, 
        s_Name='', 
        s_Type='',
        s_Status='',
        s_Visibility='',                
        s_Disk_Format='',
        s_Size='',
    ):
        self.Name = s_Name
        self.Type = s_Type  
        self.Status = s_Status  
        self.Visibility = s_Visibility  
        self.Disk_Format = s_Disk_Format  
        self.Size = s_Size

    def show_image(self):
        print(
            "{name} {type} {status} {visibility} {disk_format} {size}".format(
                name = self.Name,
                type = self.Type,
                status = self.Status,
                visibility = self.Visibility,
                disk_format = self.Disk_Format,
                size = self.Size,
            )
        )
    
class object_flavors(object):
    Name = ''
    Vcpus = ''
    Ram = ''
    Disk = ''
    Is_public = ''
    Id = ''

    def __init__(
        self, 
        s_Name = '', 
        s_Vcpus = '',
        s_Ram = '',
        s_Disk = '',
        s_Is_public = '',
        s_Id = ''
    ):
        self.Name = s_Name
        self.Vcpus = s_Vcpus
        self.Ram = s_Ram
        self.Disk = s_Disk
        self.Is_public = s_Is_public
        self.Id = s_Id

    def show_flavor(self):
        print(
            "{Name} {Vcpus} {Ram} {Disk} {Is_public} {Id}".format(
                Name = self.Name,
                Vcpus = self.Vcpus,
                Ram = self.Ram,
                Disk = self.Disk,
                Is_public = self.Is_public,
                Id = self.Id,
            )
        )

class object_networks(object):
    Name = ''
    Shared = ''
    Status = ''
    Admin_State	 = ''
    Availability_Zones = ''
    Id = ''

    def __init__(
        self, 
        s_Name = '', 
        s_Shared = '',
        s_Status = '',
        s_Admin_State = '',
        s_Availability_Zones = '',
        s_Id = ''
    ):
        self.Name = s_Name
        self.Shared = s_Shared
        self.Status = s_Status
        self.Admin_State = s_Admin_State
        self.Availability_Zones = s_Availability_Zones
        self.Id = s_Id

    def show_network(self):
        print(
            "{Name} {Shared} {Status} {Admin_State} {Availability_Zones} {Id}".format(
                Name = self.Name,
                Shared = self.Shared,
                Status = self.Status,
                Admin_State = self.Admin_State,
                Availability_Zones = self.Availability_Zones,
                Id = self.Id,
            )
        )