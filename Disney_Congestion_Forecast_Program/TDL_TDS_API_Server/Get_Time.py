import time
def Get_Time(Type):     #Type 0:str 1:timedata
    now = time.ctime()
    cnvtime = time.strptime(now)
    if Type is False:
        return(str(time.strftime("%Y-%m-%d %H:%M:%S", cnvtime)))
    else:
        return(cnvtime)
        
if __name__ == "__main__":
    pass