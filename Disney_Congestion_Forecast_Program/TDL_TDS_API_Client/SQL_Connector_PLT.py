 import mysql.connector,copy,datetime,Query
from sshtunnel import SSHTunnelForwarder

def Get_Data(ID):
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
        cursor.execute(Query.Sel_All_Wait_Time(ID))
        rows = cursor.fetchall()
        waittime,date = [],[]
        for row in rows:
            if row[0] != None and row[0] != '終日中止':
                waittime.append(int(row[0]))
            else:
                waittime.append(0)
            date.append(row[1])
        cursor.close()
        print('MySQL:Disconnected')
        db.close()
        server.stop()
        print('SSL:Close')
    return waittime,date

if __name__ == '__main__':
    pass
