#!/usr/bin/python
#-*- coding:utf-8 -*-
#############对数据库的操作######################
# import pymysql
# conn=pymysql.connect(host='192.168.0.152',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      charset='utf8')
# #创建游标（控制器）
# cur=conn.cursor()
#执行sql语句
# cur.execute('use test1;')
# cur.execute('create table biao1(name char(20),age int,sex char(10));')
# cur.execute('show tables;')
# cur.execute('insert into biao1 values("xiaohong",20,"nan"),("xiaoming",21,"nan"),("xiaoxin",19,"nv");')
# cur.execute('delete from biao1 where age=20')
# cur.execute('select * from biao1;')
#######提交#########################
#对数据库的数据进行更改的时候
# conn.commit()       #是由链接数据库的变量来提交
# #任何结果都需要有容器来接收#################
# print(cur.fetchall())                 #接收上一个sql语句执行的结果
# print(cur.fetchmany(6))      #接收上一个语句的结果，默认只接收第一行的结果  括号里面的写入数字几，就接收多少行
# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchone())
####################断开数据库#############
#  conn.close()




############循环输入###########
# import pymysql
#
# conn = pymysql.connect(host='192.168.0.152',
#                        port=3306,
#                        user='root',
#                        password='123456',
#                        charset='utf8')
# cur = conn.cursor()
# while True:
#     shuru=input('执行语句>>>')
#     if shuru=='exit':
#         conn.close()
#         print('本次操作结束')
#         break
#     else:
#         try:
#             cur.execute('{}'.format(shuru))
#             print(cur.fetchall())
#         except:
#             print('语句出现错误，请更改')
#             continue

# from day3 import doubai_Spider
# a=doubai_Spider()

# ###################爬取文字到表格中 再从表格中读取到数据库############################
import re
import requests
import xlwt
from xlutils.copy import copy
import xlrd
class  doubai_Spider(object):
    def fasong(self,p25):
        ur='https://movie.douban.com/top250?start=%s&filter='%(p25)
        head={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
        }
        qing=requests.get(url=ur,headers=head)
        html=qing.content.decode('utf=8')
        return html
    def  guolv(self,html):
        patt=re.compile('<div class="pic">(.*?)</li>',re.S)
        patc=patt.findall(html)
        for i in range(5):
            if i ==1:
                mingcheng=re.compile(' <img width="100" alt="(.*?)" src',re.S)
                mingcheng2=mingcheng.findall(str(patc))
            elif i==2:
                daoyan=re.compile('导演: (.*?)&nbsp',re.S)
                daoyan2=daoyan.findall(str(patc))
            elif i==3:
                miaoshu=re.compile('<span class="inq">(.*?)</span>',re.S)
                miaoshu2=miaoshu.findall(str(patc))
            elif i==4:
                renshu=re.compile('<span>(.*?)人评价</span>',re.S)
                renshu2=renshu.findall(str(patc))
        return mingcheng2,daoyan2,miaoshu2,renshu2
    def baocun(self,guol,p2):
        f=xlrd.open_workbook('电影信息.xls')
        new_f=copy(f)
        sheet=new_f.get_sheet(0)

        for  j in range(len(guol)):
            for k,l in enumerate(guol[j]):
                sheet.write(k+1+p2,j,l)
        new_f.save('电影信息.xls')


xinjian=xlwt.Workbook(encoding='utf-8')
sheet=xinjian.add_sheet('excel电影')
sheet.write(0,0,'名称')
sheet.write(0,1,'导演')
sheet.write(0,2,'描述')
sheet.write(0,3,'评价人数')
xinjian.save('电影信息.xls')
a=doubai_Spider()
for h in range(0,75,25):
    html=a.fasong(h)
    patc=a.guolv(html)
    a.baocun(patc,p2=h)

import pymysql
conn=pymysql.connect(host='192.168.0.152',
                     port=3306,
                     user='root',
                     password='123456',
                     charset='utf8')
cur=conn.cursor()
cur.execute('create database bu;')
cur.execute('show databases;')
print(cur.fetchall())
conn.commit()
# m=xlrd.open_workbook('电影信息.xls')
# msheet=m.sheets()[0]
# num=msheet.nrows
# for i in range(1,num):
#     n=msheet.row_values(i)
#     if i==0:
#         cur.execute('create table biao2({} char(255),{} char(255),{} char(255),{} int);'.format(n[0],n[1],n[2],n[3]))
#     else:
#         cur.execute('insert into biao2 values("%s","%s","%s","%s");'%(n[0],n[1],n[2],[3]))
#         conn.commit()