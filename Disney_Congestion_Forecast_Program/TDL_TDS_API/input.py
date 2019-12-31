import TDL_TDS_CLASS as TTC
import requests as rq
import csv

url = 'https://api.castel.jp/disney/facility?language=ja-JP&f_type=1'
data = rq.get(url).json()
datas = data['results']
facilitys = []
for data in datas:
    id = data['id']
    park = data['park']
    area_id = data['area_id']
    area_name = data['area_name']
    name = data['name']
    standby_time = data['standby_time']
    operating_status = data['operating_status']
    operating_status_cd = data['operating_status_cd']
    lat = data['lat']
    lng = data['lng']
    image_url = data['image_url']
    link_url = data['link_url']
    upd_original = data['upd_original']
    facility = TTC.facilities(id,park,area_id,area_name,name,standby_time,operating_status,operating_status_cd,lat,lng,image_url,link_url,upd_original)
    facilitys.append(facility)

with open('stanby_data.csv','w',newline='') as f:
    writer = csv.writer(f)
    for facility in facilitys:
        writer.writerow([facility.id,facility.standby_time])
