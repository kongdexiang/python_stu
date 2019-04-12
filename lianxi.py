#!/usr/bin/python
#-*- coding:utf-8 -*-
# a='abscdswdeewew'
# print(a.count('w'
# ))
# print(a.index('w'))
# b=a.split('w')print(b)
# b=['a','b','c']
# c=''.join(b)
# print(c)
# import os
# c=[]
# a=os.listdir()
# for i in a:
#     bb=i.split('.')
#     if  bb[-1]=='py':
#         c.append(i)
# print(c)

# def shanchu(x,y,z):
#     ab=list(x)
#     if y+z >= len(x):
#         for i in range(len(x)-y):
#             ab.remove(ab[y])
#     else:
#         for j in range(z):
#             ab.remove(ab[y])
#     b=''.join(ab)
#     return b
# # print(shanchu(x='asdfgweq',y=3,z=5))
# a={1,2,34,5}
# b={4,23,52,}
# print(a-b)
# 1-2+3-4+5-6.....-98+99
# m=0
# for i in range(1,99,2):
#     b=i+1
#     c=i-b
#     m+=c
# j=m+99
# print(j)
# #猜数字游戏
# import random
# for i  in  range(3):
#     aa=random.randint(1,10)
#     a=input('请输入数字：')
#     if  int(a)== aa:
#         print('恭喜您！！！中奖了')
#         break
#     elif int(a) >aa:
#         print('很遗憾！大了')
#         continue
#     else:
#         print('很遗憾！小了')
#         continue
# 判断三角形
# ab=[]
# for i in range(3):
#     a=input('输入整数')
#     ab.append(a)
# ab.sort()
# if  int(ab[0]) +int(ab[1]) > int(ab[2]):
#     if int(ab[0])**2 + int(ab[1])**2 == int(ab[2])**2:
#         print('三角形为直角三角形')
#     elif  int(ab[0])**2 + int(ab[1])*2 > int(ab[2])**2:
#         print('三角形为锐角三角形')
#     else:
#         print('三角形为钝角三角形')

#99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d'%(i,j,i*j),end='\t')
#     print('')
#质数之和
# sum=0
# for i in range(2,100):
#     for j in range(2,i+1):
#         if i%j==0:
#             break
#     if i==j:
#         sum+=i
# print(sum)
#输入三个数 第一个为字符串 第二个为下标位置，第三个为要删除的元素数
# def shanchu(x,y,z):
#     try:
#         for i in range(z):
#             x=x.replace('%s'%(x[y]),'')
#     except:
#         for i in range(len(x)-y):
#             x=x.replace('%s'%(x[y]),'')
#     return x
# print(shanchu(x='qwertdfgh',y=3,z=5))
# 把列表中最小的放在第一位，最大的放在最后一位
# a=input('输入过个数字,以逗号隔开')
# b=a.split(',')
# for i in range(len(b)):
#     for j  in range(0,len(b)):
#         if int(b[i]) > int(b[j]):
#             break
#     else:
#         b.insert(0,b[i])
#         b.pop(i+1)
# for k in range(len(b)):
#     for l in range(0,len(b)):
#         if int(b[k]) < int(b[l]):
#             break
#     else:
#         b.append(b[k])
#         b.pop(k)
# print(b)
#将字符串变为整数
# a=input('输入数字')
# b=0
# for i,j in enumerate(a[::-1]):
#     for m in range(10):
#         if j==str(m):
#             b+=m*(10**i)
# print(b)
#####读取文件内容
# f=open(r'a.txt','r',encoding='utf-8')
# b=f.readlines()
# for i in b:
#     print(i)
# f=open(r'ab.txt','w+',encoding='utf-8')
# m=open(r'a.txt','r+',encoding='utf-8')
# b=m.readlines()
# for i in b:
#     f.write(i)
# f.close()
# m.close()
#函数的命名规则  字符串 下划线 数字组合  不能以数字 下划线开头  不能命名python中的函数  不能以python中的文件命名
#加括号代表执行此函数，不加括号代表函数名
#在函数里面定义的变量为局部变量   在文件中定义的变量为全局变量  在全局范围内很有效的
#global  变量名   将局部变量变为全局变量
#必须参数 默认参数  可变长参数   格式为  def  函数名（**参数名）  参数接受的是键值对    def 函数名（*参数名）  接受的是元祖
#优先级    必须参数  默认参数  可变长参数
#匿名参数    函数名=lambda ：表达式    函数名=lambda 参数名 ：表达式
#列表推导式   将控制语句写在列表中 使产生的结果直接产生在列表中
#变量名=【变量名  控制语句】
# f=[i for i in range(10) ]
#ord() 将字符转化为ascii中的位置
#chr   将数字转化为ascii中的字符
#dirmod   整除和求和
#hex（十进制数） 十进制转十六进制
#act（十进制数） 十进制转八进制
#bin（十进制数） 十进制转二进制
#int（进制数）   其他进制转十进制数   int（0x10）十六进制转十进   int（0o10） 八进制转十进制  int（0b10）  二进制转十进制
#
import xlwt
#打开表格    f=xlwt.Workbook(encoding='utf-8')
#添加标签页   sheet=f.add_sheet('xuexi')
#写入内容   sheet.write(hang,lie,neirong)
#f.save('wenjianming.xls')
import xlrd
#读取表格内容
#打开表格读取   f=xlrd.open_workbook(wenjianming.houzhuim)
#获取有多少个标签页   f.sheets()
#获取所有的标签页    f.sheet_names()
#根据索引来获取想要操作标签页   sheet=sheets()[0]
#根据标签页名称来获取想要操作的标签页 sheet=f.sheet_by_name(mingcheng)
#获取标签页中多少行      sheet.nrows
#获取标签页第几行的内容   sheet.row_values(0)
#获取标签页有多少页      sheet.ncols
#获取第几列的内容        sheet.cols_values(0)
#获取某个单元格的内容    sheet.cell(hang,lie).value
import xlutils
from xlutils.copy import copy
#打开一个文件     f=xlrd.open_workbook(wenjianm.xls)
#复制           newf=copy(f)
#通过索引来获取想要操作的标签页   sheet=newf.get_sheet(0)
#写入内容       sheet.write(0,2,neirong)
#newf.save('mingcheng.houzhuiming')

# import os
# b=os.path.splitext(
#     r'C:\Users\kong\Desktop\python学习\ab.txt'
# )
# print(b)
# import xlrd
# f=xlrd.open_workbook('信息.xls')
# sheet=f.sheets()[0]
# nei=sheet.cell(1,0).value
# print(nei)
# f=open(r'ab.txt','r+',encoding='utf-8')
# print(f.readlines())
# import pymysql
# conn=pymysql.connect(host='192.168.0.147',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      charset='utf8')
# cur=conn.cursor()
# cur.execute('show databases;')
# cur.execute('use text;')
# cur.execute('show tables;')
# print(cur.fetchall())
# conn.commit()
# conn.close()
# import time
# a=time.localtime()
# b=time.mktime(a)
# print(b)
# class p_Spider(object):
#     x=1
# class c2_Spider(p_Spider):
#     pass
# class c1_Spider(p_Spider):
#     pass
# b=p_Spider()
# b.x=3
# print()
# import requests
# ur='http://v.gdt.qq.com/gdt_stats.fcg?viewid=8dyacVItdXg!KTEhLx48X41iUiiNl77mgvERBiVIrleO48xw5FwTJ996pKGnaKBZM_uPsaMhq!JoZc3rbfaI2tQwuFj0zproVCgsv8A7fQ0BSyQr8m3KdaxuaeOmG2W_dWRgWhmS1zHtBfP0dPQQC!jhedGWnJL3&i=1&os=0&xp=2'
# head={
#     {'Host':'v.gdt.qq.com',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
#     'Accept':'image/webp,*/*',
#     'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#     'Accept-Encoding':'gzip,deflate'
#     'Connection:keep-alive',
#     'Cookie':'_qpsvr_localtk=0.8917830262012543; pgv_pvi=9063916544; pgv_si=s9481380864; pgv_pvid=27414272; pgv_info=ssid=s5538758890; ptisp=cnc; ptui_loginuin=2215881363; uin=o2215881363; skey=@01mrpgbyj; RK=QRo13PyY1C; ptcz=3ffd0b80f0c1cc45db860c9562687a9b192b4584acf547e6bc9ab46d4ead102b'
#     }
# }
# re=requests.get(url=ur,headers=head)
# print(re)
#######################web自动化###########################

