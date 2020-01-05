#施設情報書き込み
def In_Fac_List(data):
    sql = 'INSERT INTO Facility (Facility_ID, Facility_Name, Facility_URL) VALUE ('+data.get_id()+',"'+data.get_name()+'","'+data.get_link_url()+'");'
    return sql

#待ち時間書き込み(施設IDのみ)
def In_FacID_Only(data):
    sql = 'INSERT INTO Standby_Time (Facility_ID) VALUE ('+data.get_id()+');'
    return sql

#待ち時間書き込み
def In_All(data):
    sql = 'INSERT INTO Standby_Time (Facility_ID,Standby_Time) VALUE ('+data.get_id()+',"'+data.get_standby_time()+'");'
    return sql

#Auto_Increment初期化
def A_I_Clear():
    sql = 'ALTER TABLE `Standby_Time` auto_increment = 1'
    return sql

if __name__ == "__main__":
    pass