import mysql.connector,copy
from sshtunnel import SSHTunnelForwarder

def Get_Data():
    with SSHTunnelForwarder(
        ("saichann.shop", 22),
        ssh_username="saichann",
        ssh_password="1o1gxdlSYkes",
        remote_bind_address=("127.0.0.1",3306)
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
        data = {'name':None,'average':None,'waittime':None}
        sql = 'SELECT Facility.Facility_Name,AVG(Standby_Time.Standby_Time),MAX(Standby_Time.Date) FROM saichann.Facility inner join saichann.Standby_Time ON Facility.Facility_ID = Standby_Time.Facility_ID group by Facility.Facility_Name;'
        cursor.execute(sql)
        rows = cursor.fetchall()
        n = 0
        for row in rows:
            datas.append(copy.deepcopy(data))
            datas[n]['name'] = row[0]
            datas[n]['average'] = row[1]
            n = n + 1
        sql = 'SELECT Facility.Facility_Name,Standby_Time.Standby_Time,MAX(Standby_Time.Date) FROM saichann.Facility inner join saichann.Standby_Time ON Facility.Facility_ID = Standby_Time.Facility_ID  group by Facility.Facility_Name;'
        cursor.execute(sql)
        rows = cursor.fetchall()
        n = 0
        for row in rows:
            datas[n]['waittime'] = row[1]
            n = n + 1
        cursor.close()
        db.close()
        server.stop()
    return datas
a = Get_Data()