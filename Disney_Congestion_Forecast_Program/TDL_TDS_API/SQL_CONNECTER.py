import pyodbc
from Job_Class import Job_info
#https://docs.microsoft.com/ja-jp/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-2017
#SQLSever問い合わせ
class SQL_Connection:
    #SQL接続モジュール 戻り2
    def sql_connection(self):
        #SQL Server認証
        server = 'server_name' 
        database = 'database_name' 
        username = 'user_name' 
        password = 'password' 
        print('Waiting for connection...')
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        return cursor,cnxn

