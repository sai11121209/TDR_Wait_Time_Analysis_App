import mysql.connector,Query
from sshtunnel import SSHTunnelForwarder

check_a = input('SQLサーバのStandby_Timeテーブルデータを全消去します よろしいですか?(y/n):')
if check_a == 'y':
    check_b = input('消去したのちAuto_Incrementを初期化します よろしいですか?(y/n):')
    if check_b == 'y':
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
            cursor.execute(Query.Del_All())
            db.commit()
            cursor.execute(Query.A_I_Clear())
            db.commit()
            cursor.close()
            db.close()
            server.stop()
            print('taskcomplete')