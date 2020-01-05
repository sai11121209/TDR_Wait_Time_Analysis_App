
def Print_Data(cursor):
    rows = cursor.fetchall()
    for row in rows:
        print(row[0]+':'+'待ち時間'+str(row[1])+':'+str(row[2]))

if __name__ == "__main__":
    pass