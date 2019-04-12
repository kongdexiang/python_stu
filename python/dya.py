#!/usr/bin/python
#-*- coding:utf-8 -*-
import xlrd
import  pymysql
ab=[]
conn=pymysql.connect(host='192.168.0.95',
                     port=3306,
                     user='root',
                     password='123456',
                     charset='utf8')
cur=conn.cursor()
cur.execute('show databases;')
cur.execute('use text;')
# cur.execute('create database text;')
# print(cur.fetchall())
f=xlrd.open_workbook('招聘信息.xls')
sheet=f.sheets()[0]
for j in range(sheet.ncols):
    ab.append(j)
for i in range(sheet.nrows):
    nul=sheet.row_values(i)
    if i==0:
        cur.execute('create table zhaopinxinxi(%s char(255),%s char(255),%s char(255),%s char(255),%s char(255),%s char(255));'%(nul[ab[0]],nul[ab[1]],nul[ab[2]],nul[ab[3]],nul[ab[4]],nul[ab[5]]))
        conn.commit()
    else:
        cur.execute('insert into zhaopinxinxi values("%s","%s","%s","%s","%s","%s");'%(nul[ab[0]],nul[ab[1]],nul[ab[2]],nul[ab[3]],nul[ab[4]],nul[ab[5]]))
        conn.commit()
conn.close()

####################从数据库写入到windowsexcel表格中
import pymysql
import xlwt
import  xlutils
import xlrd
from xlutils.copy import copy
conn=pymysql.connect(host='192.168.0.95',
                     port=3306,
                     user='root',
                     password='123456',
                     charset='utf8')
cur = conn.cursor()
cur.execute('use text;')
class shujuku_Spider(object):
    def neirong(self):
        cur.execute('select * from zhaopinxinxi;')
        shuju=cur.fetchall()
        return shuju
    def biaotou(self):
        cur.execute('desc zhaopinxinxi;')
        biaot=cur.fetchall()
        return biaot
    def chuangjian(self,biao):
        f=xlwt.Workbook(encoding='utf-8')
        sheet=f.add_sheet('招聘信息')
        for i,j in enumerate(biao):
            sheet.write(0,i,j[0])
            f.save('招聘.xls')
    def  xieru(self,nei):
        f=xlrd.open_workbook('招聘.xls')
        new_f=copy(f)
        sheet=new_f.get_sheet(0)
        for i,j in enumerate(nei):
            for k,l in enumerate(j):
                sheet.write(i+1,k,l)
        new_f.save('招聘.xls')
a=shujuku_Spider()
biao=a.biaotou()
a.chuangjian(biao)
nei=a.neirong()
a.xieru(nei)

 #################从数据库读取到txt文件#####################
import pymysql
conn=pymysql.connect(host='192.168.0.95',
                     port=3306,
                     user='root',
                     password='123456',
                     charset='utf8')
cur=conn.cursor()
cur.execute('use text;')
class wenjian_Spider(object):
    def biaotou(self):
        cur.execute('desc zhaopinxinxi;')
        biaot=cur.fetchall()
        return biaot
    def neirong(self):
        cur.execute('select * from zhaopinxinxi;')
        neir=cur.fetchall()
        return neir
    def xirru(self,biao,nei):
        with open(r'ab.txt','a+',encoding='utf-8') as f :
            for i in range(len(biao)):
                for j in range(len(biao[i])):
                        if j==0:
                            if biao[i] == biao[-1]:
                                f.write('%s' % (biao[i][j]))
                            else:
                                f.write('%s,'%(biao[i][j]))
            f.write('\n')
            for k in range(len(nei)):
                for l in range(len(nei[k])):
                    if nei[k][l]==nei[k][-1]:
                        f.write('%s'%(nei[k][l]))
                    else:
                        f.write('%s,'%(nei[k][l]))
                f.write('\n')

a=wenjian_Spider()
biao1=a.biaotou()
nei1=a.neirong()
a.xirru(biao=biao1,nei=nei1)
conn.close()





