#!/usr/bin/python
# -*- coding:utf-8 -*-
################爬虫###############
# import requests
# import re
# from bs4 import BeautifulSoup
# class 糗事_Spider(object):
#     def 发送请求(self,page):
#         ur='https://www.qiushibaike.com/text/page/%s/'%(page)
#         #伪装浏览器
#         head={
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
#         }
#         #发送请求的代码
#         请求=requests.get(url=ur,headers=head)
#         #读取响应 ：1  text   2.content
#         # with open(r'a.html','wb') as f :
#         #     f.write(请求.content)    #以字节码进行读取
#         # with open(r'a.html','w+',encoding='utf-8') as f:
#         #     f.write(请求.text)       #以字符串的方式进行读取
#         html=请求.content.decode('utf-8')
#         return html
#     def 过滤(self):
#         abc=[]
#         ab=self.发送请求(1)     #调用第一个方法的结果
#         patt=re.compile(r'<div class="content">(.*?)</span>',re.S)   #将正则表达式进行编译
#         items=patt.findall(ab) #将编译后的条件到字符串中去查找
#         for i in items:
#             i=i.replace('<span>','').replace('<br/>','').strip()
#             print(i)
#             abc.append(i)
#         return abc
#     def  save(self):
#         al=self.过滤()
#         with open('b.txt','a+',encoding='utf-8') as f :
#             for i in al:
#                 f.write(i+'\n')
# qiu=糗事_Spider()
# for j in range(1,6):
#     qiu.发送请求(1)
#     qiu.过滤()
#     qiu.save()

#爬糗事百科里面的新鲜里面的段子
# import requests
# import re
# class xinxian_Spider(object):
#     def qingqiu(self,page):
#         ur='https://www.qiushibaike.com/textnew/page/%s/?s=5167695'%(page)
#         head={
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
#         }
#         qing=requests.get(url=ur,headers=head)
#         html=qing.content.decode('utf-8')
#         return html
#     def shaixuan(self,page2):
#         lie=[]
#         patt=re.compile(r'<div class="content">(.*?)</div>',re.S)
#         patc=patt.findall(page2)
#         for i in patc:
#             if '<span class="contentForAll">' not in i:
#                 i=i.replace('<span>','').replace('<br/>','').replace('</span>','').strip()
#                 lie.append(i)
#             else:
#                 i=i.replace('<span class="contentForAll">查看全文</span>','').replace('<span>','').replace('<br/>','').strip()
#                 lie.append(i)
#         return lie
#     def baocun(self,qw):
#         with open(r'b.txt','a+',encoding='utf-8') as l:
#             for i in qw:
#                 l.write(i+'\n')
# qiu=xinxian_Spider()
# for j in range(1,3):
#     html=qiu.qingqiu(1)
#     wenjian=qiu.shaixuan(html)
#     qiu.baocun(wenjian)


############### 爬取豆瓣上的名称 导演 描述 评价人数####################
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

# ##############爬取图片##########################
# import os
# import re
# import requests
# class qiushi_Spider(object):
#     a=0
#     def qingqiu(self,page):
#         ur='https://www.qiushibaike.com/imgrank/page/%s/'%(page)
#         head={
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
#         }
#         res=requests.get(url=ur,headers=head)
#         html=res.content.decode('utf-8')
#         return html
#     def guolv(self,html):
#         shuju=[]
#         #过滤的是图片的网址
#         patt=re.compile(r'<div class="thumb">(.*?)</a>',re.S)
#         items=patt.findall(html)
#         for i in items:
#             abc=re.compile('src="(.*?)"',re.S)
#             hh=abc.findall(i)
#             shuju.append('https:'+hh[0])
#         return shuju
#     def  baocun(self,shu):
#         # 注：任何图片都是二进制
#         # 请求图片的网址，得到是图片的源代码
#         for j,k in enumerate(shu):
#             res=requests.get(k)
#             ht=res.content               #读取出来的即如果是一个二进制
#             with open(r'C:\Users\kong\Desktop\python学习\patu\%s.jpg'%(self.a),'wb') as f:
#                 f.write(ht)
#             self.a+=1
#     def shanchu(self):
#         aa=os.listdir(r'C:\Users\kong\Desktop\python学习\patu')
#         for i in range(len(aa)):
#             os.remove(r'C:\Users\kong\Desktop\python学习\patu\%s'%(aa[i]))
# a=qiushi_Spider()
# for i in range(1,4):
#     a.baocun(a.guolv(a.qingqiu(i)))
#
#
#
# 'https://pic.qiushibaike.com/system/pictures/12153/121537072/medium/PKRWOU07PQJE6K1C.jpg'
# 'https://pic.qiushibaike.com/system/pictures/11832/118321309/medium/app118321309.jpg'