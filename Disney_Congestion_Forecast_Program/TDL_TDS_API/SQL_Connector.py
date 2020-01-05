#MySQL/SSL_Connector
import mysql.connector
from sshtunnel import SSHTunnelForwarder

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
     
    sql = "SELECT * FROM Facility"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    db.close()
    server.stop()
