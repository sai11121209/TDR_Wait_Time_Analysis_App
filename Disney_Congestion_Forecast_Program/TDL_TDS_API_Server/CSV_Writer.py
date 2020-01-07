import pandas as pd
import time,Query,copy
def CSV_Writer(cursor,Time):
    dr = "C:/Users/sai11/OneDrive/デスクトップ/春休み/WebScrapingProgram/Disney_Congestion_Forecast_Program/TDL_TDS_Wait_Time_List/"
    Date = time.strftime("%Y_%m_%d",Time)
    print(Date)
    data = {}
    datas = {}
    now = []
    cursor.execute(Query.Sel_FacID_Only())
    rows = cursor.fetchall()
    for row in rows:
        data.setdefault(row[0])
    print(data)
    cursor.execute(Query.Sel_All())
    rows = cursor.fetchall()
    row = rows[00000]
    print(row[2].hour)
    now = [row[2].hour,row[2].minute]
    print(now)
    for row in rows:
        if now[0] != row[2].hour or now[1] < row[2].minute:
            print(data)
            datas.setdefault(str(now[0])+':'+str(now[1]))
            datas[str(now[0])+':'+str(now[1])] = copy.deepcopy(data)
            now = [row[2].hour,row[2].minute]
        else:
            data[row[0]] = row[1]
    df = pd.DataFrame(datas)
    df.sort_index(axis=0, ascending=True, inplace=True)
    print(df)
    df.T.to_csv(dr+Date+'.csv')