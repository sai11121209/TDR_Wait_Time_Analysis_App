#TDL営業時間取得
def Sel_TDL_Operating_Status():
    sql = 'SELECT Operating_Status,Operating_Status_Start,Operating_Status_End,MAX(Date) FROM Standby_Time WHERE Facility_ID = 1;'
    return sql

#TDS営業時間取得
def Sel_TDS_Operating_Status():
    sql = 'SELECT Operating_Status,Operating_Status_Start,Operating_Status_End,MAX(Date) FROM Standby_Time WHERE Facility_ID = 50;' 
    return sql

#全待ち時間取得
def Sel_All_Wait_Time(ID):
    sql = 'SELECT Standby_Time,Date FROM saichann.Standby_Time WHERE Facility_ID = '+ID+';'
    return sql

#最新待ち時間取得
##訂正部分
def Sel_Wait_Time_Latest():
    #sql = 'SELECT DataA.Facility_Name,DataA.Standby_Time.Standby_Time,DataA.Standby_Time.Date FROM Facility AS FacilityA,Standby_Time AS Standby_TimeA INNER JOIN (SELECT Facility.Facility_Name,MAX(Standby_Time.Date) AS MAXDate FROM Facility,Standby_Time GROUP BY Facility.Facicility_Name) AS DataB ON DataA.Facility.Facility_Name = DataB.Facility.Facility_Name AND DataA.Standby_Time.Date = DataB.Standby_Time.MAXDate;'
    #sql = 'SELECT  Facility.Facility_Name,Standby_Time.Standby_Time,Standby_Time.Date FROM Facility,Standby_Time AS DATA (SELECT DATAA.Facility_Name,DATAA.Stadby_Time,DATAA.Date FROM DATA AS DATAA) INNER JOIN (SELECT DATA.Facility_Name,MAX(DATA.Date) AS MAXDate FROM DATA GROUP BY DATA.Facility_Name)AS DATAB ON DATAA.Facility_Name = DATAB.Facility_Name AND DATAA.Date = DATAB.MAXDate;'
    #sql = 'SELECT * FROM Facility,Standby_Time AS data WHERE =(SELECT MAX(data.Date) FROM Facility,Standby_Time WHERE data.ID = data.ID)'
    sql = 'SELECT Facility.Facility_Name,Standby_Time.Standby_Time,MAX(Standby_Time.Date) FROM saichann.Facility inner join saichann.Standby_Time ON Facility.Facility_ID = Standby_Time.Facility_ID  group by Facility.Facility_Name;'
    return sql