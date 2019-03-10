# -*- coding: UTF-8 -*-

#定義計算商品
Product='TX'
Period='201803'

#定義開盤日期、開盤、收盤時間
Date = '20180314'
Otime ='84500'
Ctime = '134500'

#取得資料，依照逗點分隔，依照分隔符號分解欄位，去除空白
I020 = [line.replace(' ','').split(",") for line in open('Daily_2018_03_14.csv')][1:]

#取出指定商品
ProdData = [ line for line in I020 if line[1]==Product and line[2]==Period and line[0]==Date and int(line[3])>= int(Otime) and int(line[3])<= int(Ctime) ]

#定義時間轉數值函數
def TimetoNumber(time):
 time=time.zfill(6)
 sec=int(time[:2])*3600+int(time[2:4])*60+int(time[4:6])
 return sec

#定義相關變數
MAarray = []
MA = []
MAValue = 0
STime = TimetoNumber('84500')
Cycle = 60
MAlen = 10

#開始進行MA計算
for i in ProdData:
 time=i[3]
 price=int(i[4])
 if len(MAarray)==0:
  MAarray+=[price]
 else:
  if TimetoNumber(time)<STime+Cycle:
   MAarray[-1]=price
  else:
   if len(MAarray)==MAlen:
    MAarray=MAarray[1:]+[price]
   else:
    MAarray+=[price]   
   STime = STime+Cycle
 MAValue=float(sum(MAarray))/len(MAarray)
 MA.extend([[time,MAValue]])
 print time,MAValue
