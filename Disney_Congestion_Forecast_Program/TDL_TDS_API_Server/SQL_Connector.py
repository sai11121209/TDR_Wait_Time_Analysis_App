#MySQL/SSL_Connector
import mysql.connector,os,time,Query,CSV_Writer
from sshtunnel import SSHTunnelForwarder
from Download_Data import Download_Data
from Get_Time import Get_Time
from Print_Data import Print_Data

#waittime = int(input('データ取得間隔指定(分):'))
waittime = 5
#開園時刻閉園時刻取得
while(1):
    Timedata = Get_Time(1)
    Time_H = int(time.strftime("%H",Timedata))
    Time_M = int(time.strftime("%M",Timedata))
    Time_S = int(time.strftime("%S",Timedata))
    if Time_M % waittime == 0 and Time_S == 0 :
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
                #sql = Query.In_Fac_List(data)
                #print(sql)
                #cursor.execute(sql)
                #db.commit()
            for data in datas:
                if len(data.get_standby_time()) == 0:
                    sql = Query.In_FacID_Only(data)
                else:
                    sql = Query.In_All(data)
                print(sql,end='')
                cursor.execute(sql)
                print('ok')
            db.commit()
            cursor.close()
            db.close()
            server.stop()
            print('Current Time:'+time.strftime("%Y/%m/%d %H:%M:%S", Get_Time(0)))
        time.sleep(waittime*50)
    if Time_H == 22:
        break
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
    #Print_Data(cursor)
    CSV_Writer.CSV_Writer(cursor,Timedata)
    cursor.execute(Query.Del_All())
    db.commit()
    cursor.execute(Query.A_I_Clear())
    db.commit()
    cursor.execute(Query.T_Opt())
    db.commit()
    cursor.close()
    db.close()
    server.stop()