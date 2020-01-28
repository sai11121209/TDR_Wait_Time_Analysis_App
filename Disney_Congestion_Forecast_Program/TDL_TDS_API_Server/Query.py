#施設情報書き込み
def In_Fac_List(data):
    sql = 'INSERT INTO Facility (Facility_ID, Facility_Name, Facility_URL) VALUE ('+data.get_id()+',"'+data.get_name()+'","'+data.get_link_url()+'");'
    return sql


#待ち時間書き込み(施設IDのみ)
def In_FacID_Only(data):
    sql = 'INSERT INTO Standby_Time (Facility_ID) VALUE ('+data.get_id()+');'
    return sql

#待ち時間書き込み(施設ID,営業時間のみ)
def In_Fac_Sta_Only(data):
    operating_status_time = data.get_operating_status()[1].split('-')
    sql = 'INSERT INTO Standby_Time (Facility_ID,Operating_Status,Operating_Status_Start,Operating_Status_End) VALUE ('+data.get_id()+',"'+data.get_operating_status()[0]+'","'+operating_status_time[0]+'","'+operating_status_time[1]+'");'
    return sql

#待ち時間書き込み(施設ID,待ち時間のみ)
def In_Fac_WT_Only(data):
    sql = 'INSERT INTO Standby_Time (Facility_ID,Standby_Time) VALUE ('+data.get_id()+',"'+data.get_standby_time()+'");'
    return sql

#待ち時間書き込み(施設ID,待ち時間,営業時間)
def In_All(data):
    operating_status_time = data.get_operating_status()[1].split('-')
    sql = 'INSERT INTO Standby_Time (Facility_ID,Standby_Time,Operating_Status,Operating_Status_Start,Operating_Status_End) VALUE ('+data.get_id()+',"'+data.get_standby_time()+'","'+data.get_operating_status()[0]+'","'+operating_status_time[0]+'","'+operating_status_time[1]+'");'
    return sql

#施設情報取得
def Sel_FacID_FacName():
    sql = 'SELECT Facility.Facility_Name FROM saichann.Facility inner join saichann.Standby_Time ON Facility.Facility_ID = Standby_Time.Facility_ID  group by Facility.Facility_Name;'
    return sql

#最新待ち時間取得
def Sel_Wait_Time_Latest():
    sql = 'SELECT Facility.Facility_Name,Standby_Time.Standby_Time,MAX(Standby_Time.Date) FROM saichann.Facility inner join saichann.Standby_Time ON Facility.Facility_ID = Standby_Time.Facility_ID  group by Facility.Facility_Name;'
    return sql

#待ち時間csv書き出し
def Sel_All():
    sql = 'SELECT Standby_Time.Facility_ID,Standby_Time.Standby_Time,Standby_Time.Date FROM Standby_Time WHERE (Standby_Time.Standby_Time,Standby_Time.Date) IN (SELECT Standby_Time.Standby_Time,Standby_Time.Date FROM Facility inner join saichann.Standby_Time ON Facility.Facility_ID = Standby_Time.Facility_ID group by Facility.Facility_ID ORDER BY Standby_Time.Date ASC,Facility.Facility_ID ASC);'
    return sql

#待ち時間csv書き出し(施設IDのみ)
def Sel_FacID_Only():
    sql = 'SELECT Facility.Facility_ID FROM saichann.Facility inner join saichann.Standby_Time ON Facility.Facility_ID = Standby_Time.Facility_ID  group by Facility.Facility_Name;'
    return sql

#待ち時間データ全消去
def Del_All():
    sql = 'TRUNCATE `Standby_Time` ;'
    return sql

#Auto_Increment初期化
def A_I_Clear():
    sql = 'ALTER TABLE `Standby_Time` auto_increment = 1'
    return sql

#テーブルの最適化
def T_Opt():
    sql = 'OPTIMIZE TABLE `Standby_Time`;'
    return sql

if __name__ == "__main__":
    pass