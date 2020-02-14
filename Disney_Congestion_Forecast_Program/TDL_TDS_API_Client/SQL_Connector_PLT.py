import mysql.connector,copy,datetime,Query
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
        data = {'ID':None,'name':None,'average':None,'waittime':None,'op_status':None,'fp_status':None,'fp_s':None,'fp_e':None,'time':None}
        facdatadic = {}
        infdatadic = {'waittime':[],'time':[]}
        cursor.execute(Query.Sel_Wait_Time_Avg())
        rows = cursor.fetchall()
        n = 0
        for row in rows:
            datas.append(copy.deepcopy(data))
            datas[n]['ID'] = row[0]
            datas[n]['name'] = row[1]
            datas[n]['average'] = row[2]
            datas[n]['op_status'] = row[3]
            datas[n]['op_s'] = row[4]
            datas[n]['op_e'] = row[5]
            datas[n]['fp_status'] = row[6]
            datas[n]['fp_s'] = row[7]
            datas[n]['fp_e'] = row[8]
            n += 1
        times = []
        cursor.execute(Query.Sel_TDL_Operating_Status())
        times.append(cursor.fetchone())
        cursor.execute(Query.Sel_TDS_Operating_Status())
        times.append(cursor.fetchone())
        print(times)
        cursor.execute(Query.Sel_Wait_Time_Latest())
        rows = cursor.fetchall()
        n = 0
        for row in rows:
            datas[n]['waittime'] = row[1]
            datas[n]['time'] = row[2]
            n = n + 1
        ##新規
        #cursor.execute(Query.Sel_All_Wait_Time())
        #rows = cursor.fetchall()
        #for row in rows:
            #if row[0] != None and row[0] != '終日中止':
                #facdatadic[row[2]]['waittime'].append(int(row[0]))
            #else:
                #facdatadic[row[2]]['waittime'].append(0)
            #facdatadic[row[2]]['time'].append(row[1])
        #print(facdatadic)
        ##終わり
        cursor.close()
        print('MySQL:Disconnected')
        db.close()
        server.stop()
        print('SSL:Close')
    return datas,times

if __name__ == '__main__':
    pass