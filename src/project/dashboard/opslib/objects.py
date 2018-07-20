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
        

