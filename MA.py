# -*- coding: UTF-8 -*-

#�w�q�p��ӫ~
Product='TX'
Period='201803'

#�w�q�}�L����B�}�L�B���L�ɶ�
Date = '20180314'
Otime ='84500'
Ctime = '134500'

#���o��ơA�̷ӳr�I���j�A�̷Ӥ��j�Ÿ��������A�h���ť�
I020 = [line.replace(' ','').split(",") for line in open('Daily_2018_03_14.csv')][1:]

#���X���w�ӫ~
ProdData = [ line for line in I020 if line[1]==Product and line[2]==Period and line[0]==Date and int(line[3])>= int(Otime) and int(line[3])<= int(Ctime) ]

#�w�q�ɶ���ƭȨ��
def TimetoNumber(time):
 time=time.zfill(6)
 sec=int(time[:2])*3600+int(time[2:4])*60+int(time[4:6])
 return sec

#�w�q�����ܼ�
MAarray = []
MA = []
MAValue = 0
STime = TimetoNumber('84500')
Cycle = 60
MAlen = 10

#�}�l�i��MA�p��
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
