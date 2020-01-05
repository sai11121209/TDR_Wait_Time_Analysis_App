#MySQL/SSL_Connector
import mysql.connector
from sshtunnel import SSHTunnelForwarder
from Download_Data import Download_Data
import time,os

while(1):
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
        cursor = db.cursor(named_tuple=True)
        datas = Download_Data()
        #for data in datas:
            #sql = 'INSERT INTO Facility (Facility_ID, Facility_Name, Facility_URL) VALUE ('+data.get_id()+',"'+data.get_name()+'","'+data.get_link_url()+'");'
            #print(sql)
            #cursor.execute(sql)
            #db.commit()
        for data in datas:
            if len(data.get_standby_time()) == 0:
                sql = 'INSERT INTO Standby_Time (Facility_ID) VALUE ('+data.get_id()+');'
            else:
                sql = 'INSERT INTO Standby_Time (Facility_ID,Standby_Time) VALUE ('+data.get_id()+',"'+data.get_standby_time()+'");'
            print(sql)
            cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        server.stop()
    time.sleep(300)
    print('-------------------------')
