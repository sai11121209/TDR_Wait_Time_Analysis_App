#MySQL/SSL_Connector
import mysql.connector,os,time,Query,CSV_Writer,API_Download_Data
from sshtunnel import SSHTunnelForwarder
from Get_Time import Get_Time
from Print_Data import Print_Data

#waittime = int(input('データ取得間隔指定(分):'))
waittime = 1
#開園時刻閉園時刻取得
uploadlogs = []
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
            #datas = API_Download_Data.Fac_det_Data_Get()
            #for data in datas:
                #sql = Query.In_Fac_List(data)
                #cursor.execute(sql)
                #db.commit()
            datas = API_Download_Data.Fac_Inf_Data_Get()
            for data in datas:
                if data['standbyTimeDisplayType'] == 'HIDE':
                    if 'facilityStatusMessage' in data:
                        sql = Query.In_FacID_Only(data)
                    else:
                        sql = Query.In_FacID_Only_F(data)
                elif data['standbyTimeDisplayType'] == 'NORMAL':
                    if 'fastPassStatus' in data:
                        if data['fastPassStatus'] == 'TICKETING':
                            sql = Query.In_All_T(data)
                        else:
                            sql = Query.In_All_E(data)
                    else:
                        sql = Query.In_Fac_WT_Only(data)
                else:
                    sql = Query.In_Fac_Sta_Only(data)
                print(sql,end='')
                cursor.execute(sql)
                print('ok')
            db.commit()
            cursor.close()
            db.close()
            server.stop()
            uploadlogs.append(time.strftime("%Y/%m/%d %H:%M:%S", Get_Time(0)))
            os.system('cls')
            for uploadlog in uploadlogs:
                print('Upload Time:'+uploadlog)
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