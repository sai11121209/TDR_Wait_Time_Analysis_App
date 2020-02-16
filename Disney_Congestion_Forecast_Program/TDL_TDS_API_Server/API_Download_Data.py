import API_List as API
import requests as rq

def Fac_det_Data_Get():
    datas = API.Get_API_Fac_Det()
    return datas

def Fac_Inf_Data_Get():
    datas = API.Get_API_Fac_Inf()
    return datas
    
if __name__ == "__main__":
    pass