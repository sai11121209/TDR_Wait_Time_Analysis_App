class facilities:
    def __init__(self,id,park,area_id,area_name,name,standby_time,operating_status,operating_status_cd,lat,lng,image_url,link_url,upd_original):
        self.set_id(id)
        self.set_park(park)
        self.set_area_id(area_id)
        self.set_area_name(area_name)
        self.set_name(name)
        self.set_standby_time(standby_time)
        self.set_operating_status(operating_status)
        self.set_operating_status_cd(operating_status_cd)
        self.set_lat(lat)
        self.set_lng(lng)
        self.set_image_url(image_url)
        self.set_link_url(link_url)
        self.set_upd_original(upd_original)

    #ID
    def set_id(self,id):
        self.id = id
    def get_id(self):
        return self.id

    #Park_Name
    def set_park(self,park):
        self.park = park
    def get_park(self):
        return  self.park

    #Area_ID
    def set_area_id(self,area_id):
        self.area_id = area_id
    def get_area_id(self):
        return  self.area_id

    #Area_Name
    def set_area_name(self,area_name):
        self.area_name = area_name
    def get_area_name(self):
        return  self.area_name

    #Name
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return  self.name

    #Standby_Time
    def set_standby_time(self,standby_time):
        self.standby_time = standby_time
    def get_standby_time(self):
        return  self.standby_time

    #Operating_Status
    def set_operating_status(self,operating_status):
        self.operating_status = operating_status 
    def get_operating_status(self):
        return  self.operating_status

    #Operating_Status_Cd
    def set_operating_status_cd(self,operating_status_cd):
        self.operating_status_cd = operating_status_cd
    def get_operating_status_cd(self):
        return  self.operating_status_cd

    #FastPass
    def set_fp_status(self,fp_status):
        self.fp_status = fp_status
    def get_fp_status(self):
        return  self.fp_status

    #Facility_Lat
    def set_lat(self,lat):
        self.lat = lat
    def get_lat(self):
        return  self.lat

    #Facility_Lng
    def set_lng(self,lng):
        self.lng = lng
    def get_lng(self):
        return  self.lng

    #Image_Url
    def set_image_url(self,image_url):
        self.image_url = image_url
    def get_image_url(self):
        return  self.image_url

    #Link_Url
    def set_link_url(self,link_url):
        self.link_url = link_url
    def get_link_url(self):
        return  self.link_url

    #Upd_Original
    def set_upd_original(self,upd_original):
        self.upd_original = upd_original
    def get_upd_original(self):
        return  self.upd_original