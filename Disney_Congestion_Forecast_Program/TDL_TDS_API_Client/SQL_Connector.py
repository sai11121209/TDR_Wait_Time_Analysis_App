import mysql.connector,copy,datetime
from sshtunnel import SSHTunnelForwarder

def Get_Data():
    with SSHTunnelForwarder(
        ("saichann.shop", 22),
        ssh_username="saichann",
        ssh_password="1o1gxdlSYkes",
        remote_bind_address=("127.0.0.1", 3306)
    ) as server:
        server.start()
        print('SSL:ok')
        connect_args = {
            "host": "localhost",
            "port": server.local_bind_port,
            "user": "saichann",
            "password": "Yuta1209",
            "database" : 'saichann',
        }
        
        db = mysql.connector.connect(**connect_args)
        print('MySQL:'+str(db.is_connected()))
        db.ping(reconnect=True)
        cursor = db.cursor(named_tuple=False)
        datas = []
        data = {'name':None,'average':None,'waittime':None,'time':None}
        sql = 'SELECT Facility.Facility_Name,AVG(Standby_Time.Standby_Time),MAX(Standby_Time.Date) FROM Facility inner join Standby_Time ON Facility.Facility_ID = Standby_Time.Facility_ID group by Facility.Facility_Name;'
        cursor.execute(sql)
        rows = cursor.fetchall()
        n = 0
        for row in rows:
            datas.append(copy.deepcopy(data))
            datas[n]['name'] = row[0]
            datas[n]['average'] = row[1]
            n = n + 1
        times = []
        sql = 'SELECT Operating_Status,Operating_Status_Start,Operating_Status_End,MAX(Date) FROM Standby_Time WHERE Facility_ID = 1;'
        cursor.execute(sql)
        times.append(cursor.fetchone())
        sql = 'SELECT Operating_Status,Operating_Status_Start,Operating_Status_End,MAX(Date) FROM Standby_Time WHERE Facility_ID = 50;' 
        cursor.execute(sql)
        times.append(cursor.fetchone())
        #sql = 'SELECT DataA.Facility_Name,DataA.Standby_Time.Standby_Time,DataA.Standby_Time.Date FROM Facility AS FacilityA,Standby_Time AS Standby_TimeA INNER JOIN (SELECT Facility.Facility_Name,MAX(Standby_Time.Date) AS MAXDate FROM Facility,Standby_Time GROUP BY Facility.Facicility_Name) AS DataB ON DataA.Facility.Facility_Name = DataB.Facility.Facility_Name AND DataA.Standby_Time.Date = DataB.Standby_Time.MAXDate;'
        #sql = 'SELECT  Facility.Facility_Name,Standby_Time.Standby_Time,Standby_Time.Date FROM Facility,Standby_Time AS DATA (SELECT DATAA.Facility_Name,DATAA.Stadby_Time,DATAA.Date FROM DATA AS DATAA) INNER JOIN (SELECT DATA.Facility_Name,MAX(DATA.Date) AS MAXDate FROM DATA GROUP BY DATA.Facility_Name)AS DATAB ON DATAA.Facility_Name = DATAB.Facility_Name AND DATAA.Date = DATAB.MAXDate;'
        #sql = 'SELECT * FROM Facility,Standby_Time AS data WHERE =(SELECT MAX(data.Date) FROM Facility,Standby_Time WHERE data.ID = data.ID)'
        #正常
        sql = 'SELECT  Facility.Facility_Name,Standby_Time.Standby_Time,MAX(Standby_Time.Date) FROM saichann.Facility inner join saichann.Standby_Time ON Facility.Facility_ID = Standby_Time.Facility_ID  group by Facility.Facility_Name;'
        cursor.execute(sql)
        rows = cursor.fetchall()
        n = 0
        for row in rows:
            datas[n]['waittime'] = row[1]
            datas[n]['time'] = row[2]
            n = n + 1
        cursor.close()
        print('MySQL:Disconnected')
        db.close()
        server.stop()
        print('SSL:Close')
    return datas,times

if __name__ == '__main__':
    pass