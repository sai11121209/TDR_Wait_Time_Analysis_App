#TDL営業時間取得
def Sel_TDL_Operating_Status():
    sql = 'SELECT Operating_Status,Operating_Status_Start,Operating_Status_End,MAX(Date) FROM Standby_Time WHERE Facility_Code = 194;'
    return sql

#TDS営業時間取得
def Sel_TDS_Operating_Status():
    sql = 'SELECT Operating_Status,Operating_Status_Start,Operating_Status_End,MAX(Date) FROM Standby_Time WHERE Facility_Code = 235;' 
    return sql

#全待ち時間取得
#起動時高負荷のため一時無効
#def Sel_All_Wait_Time():
    #sql = 'SELECT Standby_Time,Date,Facility_ID FROM Standby_Time;'
    #return sql

#全待ち時間取得
def Sel_All_Wait_Time(ID):
    sql = 'SELECT Standby_Time,Date,Facility_Code FROM Standby_Time WHERE Facility_Code = '+str(ID)+';'
    return sql

#待ち時間平均取得
#ここの記述追記
def Sel_Wait_Time_Avg():
    sql = 'SELECT Standby_Time.Facility_Code,Facility.Facility_Name,AVG(Standby_Time.Standby_Time) FROM Facility inner join Standby_Time ON Facility.Facility_Code = Standby_Time.Facility_Code group by Facility.Facility_Name ORDER BY Standby_Time.Facility_Code ASC;'
    return sql

#最新待ち時間取得
def Sel_Wait_Time_Latest():
    sql = 'SELECT Standby_TimeA.Facility_Code,Standby_TimeA.Standby_Time,Standby_TimeA.Date,Standby_TimeA.Operating_Status,Standby_TimeA.Operating_Status_Start,Standby_TimeA.Operating_Status_End,Standby_TimeA.Facility_FastPass_Status,Standby_TimeA.Facility_FastPass_Start,Standby_TimeA.Facility_FastPass_End FROM saichann.Standby_Time AS Standby_TimeA INNER JOIN (SELECT Facility_Code, MAX(Date) AS MaxDate FROM saichann.Standby_Time GROUP BY Facility_Code) AS Standby_TimeB ON Standby_TimeA.Facility_Code = Standby_TimeB.Facility_Code AND Standby_TimeA.Date = Standby_TimeB.MaxDate ORDER BY Standby_TimeA.Facility_Code ASC;'
    return sql