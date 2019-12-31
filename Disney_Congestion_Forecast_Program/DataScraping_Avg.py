import requests
from bs4 import BeautifulSoup
import csv

datas = []
day = 1
n = 12
for year in range(2015,2020):
    url = 'https://dwait.net/index.php/kako/kakotdr?month='+str(year)+'-01'

    r = requests.get(url)

    soup = BeautifulSoup(r.content,"lxml")
    #ディズニーランドスクレイピング
    soup = soup.body.find('div',id='container').find('div',id='body').find('div',id='body-in').main.find('div',id='main').find('div',id='post-230').find('article',class_='article').find('div',id='the-content').find('ul',class_='navi')
    copy = soup
    if year == 2019:
        n = 7
    for i in range(n):
        copy = copy.findAll('li',class_='tablefloat')[i]    #月
        for j in range(1,len(copy.find('table',class_='cal-date').findAll('tr'))):
            copya = copy.find('table',class_='cal-date').findAll('tr')[j]    #1~行数指定
            out = len(copya.findAll('td',class_='na'))
            if len(copya.findAll('td',class_='sat')) == 0:
                ran = range(1,len(copya.findAll('td'))-out)
            else:
                ran = range(1+out,len(copya.findAll('td')))
            for k in ran:
                copyb = copya.findAll('td')[k]
                landmax = 0
                seamax = 0
                for l in range(2):
                    if l == 0:
                        if len(copyb.findAll('a',class_='acal')[l].findAll('div',class_='rank')) == 2:
                            for m in range(2):
                                if len(copyb.findAll('a',class_='acal')[l].findAll('div',class_='rank')[m].text) != 1:
                                    if landmax <= int(copyb.findAll('a',class_='acal')[l].findAll('div',class_='rank')[m].text):
                                        landmax = int(copyb.findAll('a',class_='acal')[l].findAll('div',class_='rank')[m].text)#ランド
                        else:  
                            if len(copyb.findAll('a',class_='acal')[l].find('div',class_='rank').text) != 1:
                                landmax = int(copyb.findAll('a',class_='acal')[l].find('div',class_='rank').text)
                                print(landmax)
                            else:
                                landmax = 45
                    if l == 1:
                        if len(copyb.findAll('a',class_='acal')[l].findAll('div',class_='rank')) == 2:
                            for m in range(2):
                                if len(copyb.findAll('a',class_='acal')[l].findAll('div',class_='rank')[m].text) != 1:
                                    if seamax <= int(copyb.findAll('a',class_='acal')[l].findAll('div',class_='rank')[m].text):
                                        seamax = int(copyb.findAll('a',class_='acal')[l].findAll('div',class_='rank')[m].text)#シー
                        else:
                            if len(copyb.findAll('a',class_='acal')[l].find('div',class_='rank').text) != 1:
                                seamax = int(copyb.findAll('a',class_='acal')[l].find('div',class_='rank').text)
                            else:
                                seamax = 45
                datas.append([str(year),str(i+1),str(day),str(landmax),str(seamax)])
                day += 1
        copy = soup
        day = 1

print(datas)

with open('tdl_tds.csv', 'w', newline="") as f:
    header = ['year','month','day','land','sea']
    writer = csv.writer(f)
    writer.writerow(header)
    for data in datas:
        writer.writerow(data)
    