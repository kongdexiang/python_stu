#!/usr/bin/python
#-*- coding:utf-8 -*-
# import day2
# a=day2.xiaoxin()
# a.buhao()
#用素数之和表示大于等于6的偶数
# asr=[]
# for i in range(2,100):
#     for j in range(2,i+1):
#         if i%j ==0:
#             break
#     if i==j:
#         asr.append(i)
# for l in range(6,100):
#     if l%2==0:
#         for k in asr:
#             for y in asr:
#                 if k+y==l:
#                     print(k,y)
################## 面向对象########################

# a=[i**2 for i in range(1,21) ]
# print(a[9])

# def  shanchu(s,a1,a2):
#     for i in range(a2):
#         if a2==0:
#             break
#         else:
#             s=s.replace(s[a1+a2-i-1],'')
#     return print(s)
# shanchu('wqertwsf',2,0)
#从a1位置开始，向后加a2个数，删除，并向结果赋值
# def shanchu(s,a1,a2=0):
#     for i in range(len(s[a1:(a1+a2)])):
#         s=s.replace(s[a1],'')
#     return print(s)
# shanchu('wqertyasd',0,a2=2)

# s=open(r'a.txt','w',encoding='utf-8')
#
# ########将文件的内容打印到excel表格中###########
# import xlwt
# import xlutils
# with open(r'a.txt','r+',encoding='utf-8') as f:
#     asr=f.readlines()
# print(asr)
# y=xlwt.Workbook(encoding='utf-8')
# sheet=y.add_sheet('excel学习')
# for i,j in enumerate(asr):
#     sq=j.replace('\n','').split(',')
#     for l in range(len(sq)):
#         sheet.write(i,l,sq[l])
# y.save('信息.xls')
# #####################将excel中的内容打印到文件中################


#############删除文件#################################
# import os
# aa=os.listdir(r'C:\Users\kong\Desktop\python学习\patu')
# for i in range(len(aa)):
#     os.remove(r'C:\Users\kong\Desktop\python学习\patu\%s'%(aa[i]))


# javascript: s=document.documentElement.outerHTML;document.write("");document.body.innerText=s; '
#
import requests
class zixun_Spider(object):
    def qingqiu(self):
        ur = 'https://www.freebuf.com/news'
        head={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
        }
        qing=requests.get(url=ur,headers=head)
        html=qing.content.decode('utf-8')
        return html
a=zixun_Spider()
print(a.qingqiu())