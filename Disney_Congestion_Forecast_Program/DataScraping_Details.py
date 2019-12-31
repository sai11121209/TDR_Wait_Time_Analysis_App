import requests
from bs4 import BeautifulSoup
import csv
import copy

datas = []
day = 1
n = 12
for year in range(2015,2016):
    url = 'https://dwait.net/index.php/kako/kakotdr?month=2015-01&day1=2015-01-01&park=ts#waittimes'
    r = requests.get(url)

    soup = BeautifulSoup(r.content,"lxml")
    #ディズニーランドスクレイピング
    soup = soup.body.find('div',id='container').find('div',id='body').find('div',id='body-in').main.find('div',id='main').find('div',id='post-230').find('article',class_='article').find('div',id='the-content').find('article',id='panels').find('div',class_='container').find('section',id='panel-2').main.find('table',class_='waittime').tbody
    copy = soup
    copy = copy.findAll('tr')[0]
    print(len(copy.findAll('th')))
    for i in range(1,len(soup.findAll('th'))):
        copy = copy.findAll('th')[i].find('span',class_='hyou1')
        print(copy.text)
print(datas)

#with open('tdl_tds.csv', 'w') as f:
#    header = ['year','month','day','land','sea']
#    writer = csv.writer(f)
#    writer.writerow(header)
#    for data in datas:
#        writer.writerow(data)
    