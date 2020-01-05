#MySQL/SSL_Connector
import mysql.connector,os,time
from sshtunnel import SSHTunnelForwarder
from Download_Data import Download_Data
from Get_Time import Get_Time

waittime = int(input('データ取得間隔指定(分):'))

while(1):
    Timedata = Get_Time(1)
    Time_H = int(time.strftime("%H",Timedata))
    Time_M = int(time.strftime("%M",Timedata))
    Time_S = int(time.strftime("%S",Timedata))
    if Time_M % waittime == 0 and Time_S == 57 :
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
                print(sql,end='')
                cursor.execute(sql)
                print('ok')
                print('')
            db.commit()
            cursor.close()
            db.close()
            server.stop()
        print(f"The next data acquisition time is {Time_H}:{Time_M+waittime}:{Time_S}")
        time.sleep(waittime*60)
    #sql = 'ALTER TABLE `Standby_Time` auto_increment = 1'
