import Time_Transform as TT
#施設情報書き込み
def In_Fac_List(data):
    sql = 'INSERT INTO Facility (Facility_Code, Facility_ID, Facility_Park_Type, Facility_Name, Facility_Img) VALUE ('+data['facilityCode']+','+str(data['id'])+',"'+data['parkType']+'","'+data['name'].replace('"',' ')+'","'+data['images'][0]+'");'
    print(sql)
    return sql


#待ち時間書き込み(施設IDのみ)
def In_FacID_Only(data):
    sql = 'INSERT INTO Standby_Time (Facility_Code, Operating_Status) VALUE ('+data['facilityCode']+',"'+data['facilityStatusMessage']+'");'
    return sql

#待ち時間書き込み(施設IDのみ)
#戻り値バグ
def In_FacID_Only_F(data):
    sql = 'INSERT INTO Standby_Time (Facility_Code, Operating_Status, Operating_Status_Start, Operating_Status_End) VALUE ('+data['facilityCode']+',"'+data['operatings'][0]['operatingStatusMessage']+'","'+TT.Time_Transform(data,'startAt')+'","'+TT.Time_Transform(data,'endAt')+'");'
    return sql

#待ち時間書き込み(施設ID,営業時間のみ)
def In_Fac_Sta_Only(data):
    sql = 'INSERT INTO Standby_Time (Facility_Code, Operating_Status, Operating_Status_Start, Operating_Status_End) VALUE ('+data['facilityCode']+',"運営中","'+TT.Time_Transform(data,'startAt')+'","'+TT.Time_Transform(data,'endAt')+'");'
    return sql

#待ち時間書き込み(施設ID,待ち時間のみ)
def In_Fac_WT_Only(data):
    sql = 'INSERT INTO Standby_Time (Facility_Code, Standby_Time, Operating_Status, Operating_Status_Start, Operating_Status_End) VALUE ('+data['facilityCode']+','+str(data['standbyTime'])+',"運営中","'+TT.Time_Transform(data,'startAt')+'","'+TT.Time_Transform(data,'endAt')+'");'
    return sql

#待ち時間書き込み(施設ID,待ち時間,ファストパス)
def In_All_T(data):
    sql = 'INSERT INTO Standby_Time (Facility_Code, Standby_Time, Operating_Status, Operating_Status_Start, Operating_Status_End, Facility_FastPass_Status, Facility_FastPass_Start, Facility_FastPass_End) VALUE ('+data['facilityCode']+','+str(data['standbyTime'])+',"運営中","'+TT.Time_Transform(data,'startAt')+'","'+TT.Time_Transform(data,'endAt')+'","発行中","'+str(data['fastPassStartAt'])+'","'+str(data['fastPassEndAt'])+'");'
    return sql

#待ち時間書き込み(施設ID,待ち時間,ファストパス)
def In_All_E(data):
    sql = 'INSERT INTO Standby_Time (Facility_Code, Standby_Time, Operating_Status, Operating_Status_Start, Operating_Status_End, Facility_FastPass_Status) VALUE ('+data['facilityCode']+','+str(data['standbyTime'])+',"運営中","'+TT.Time_Transform(data,'startAt')+'","'+TT.Time_Transform(data,'endAt')+'","発行終了");'
    return sql

#施設情報取得
def Sel_FacID_FacName():
    sql = 'SELECT Facility.Facility_Name FROM saichann.Facility inner join saichann.Standby_Time ON Facility.Facility_Code = Standby_Time.Facility_Code  group by Facility.Facility_Name;'
    return sql

#最新待ち時間取得
def Sel_Wait_Time_Latest():
    sql = 'SELECT Facility.Facility_Name,Standby_Time.Standby_Time,MAX(Standby_Time.Date) FROM saichann.Facility inner join saichann.Standby_Time ON Facility.Facility_Code = Standby_Time.Facility_Code  group by Facility.Facility_Name;'
    return sql

#待ち時間csv書き出し
def Sel_All():
    sql = 'SELECT Standby_Time.Facility_Code,Standby_Time.Standby_Time,Standby_Time.Date FROM Standby_Time WHERE (Standby_Time.Standby_Time,Standby_Time.Date) IN (SELECT Standby_Time.Standby_Time,Standby_Time.Date FROM Facility inner join saichann.Standby_Time ON Facility.Facility_Code = Standby_Time.Facility_Code group by Facility.Facility_Code ORDER BY Standby_Time.Date ASC,Facility.Facility_Code ASC);'
    return sql

#待ち時間csv書き出し(施設IDのみ)
def Sel_FacID_Only():
    sql = 'SELECT Facility.Facility_Code FROM saichann.Facility inner join saichann.Standby_Time ON Facility.Facility_Code = Standby_Time.Facility_Code  group by Facility.Facility_Name;'
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