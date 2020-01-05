import pandas as pd
import time
def CSV_Writer(cursor,Time):
    dr = "C:/Users/sai11/OneDrive/デスクトップ/春休み/DisneyWaitTimeList"
    Date = time.strftime("%Y%M%D",Time)
    rows = cursor.fetchall()
    label = []
    for row in rows:
        label.append(row[0])
    print(label)
    for row in rows:
        pd.DataFrame([row])
    #pd.to_csv(dr+Date)