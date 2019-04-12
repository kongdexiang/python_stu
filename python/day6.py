#!/usr/bin/python
#-*- coding:utf-8 -*-
############爬取资讯里面的图片################x
# import re
# import requests
# import json
# class zixun_Spider(object):
#     def qingqiu(self):
#         ur = 'https://www.freebuf.com/newsjavascript:s=document.documentElement.outerHTML;document.write("");document.body.innerText=s; '
#         head={
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
#         }
#         qing=requests.get(url=ur,headers=head)
#         html=qing.content.decode('utf-8')
#         return html
#     def guolv(self,html):
#         ab=[]
#         patt=re.compile('<div class="news-img">(.*?)</a></div>',re.S)
#         patc=patt.findall(html)
#         for i in patc:
#             patt2=re.compile('img calss="img-responsive" src="(.*?)" title="BUF早餐铺')
#             ab.append(patt2)
#         return ab
#     def baocun(self,cc):
#         for l,k in enumerate(cc):
#             res=requests.get(k)
#             htm=res.content
#             with open(r'C:\Users\kong\Desktop\python学习\patu\%s.png'%(l),'wb') as f :
#                 f.write(cc[html])
#
# a=zixun_Spider()
# html=a.qingqiu()
# print(html)

#######################爬取逗图网图片##########################
import re
import json
import requests
import os
class doutu_Spider(object):
    def qingqiu(self,n):
        ur='https://www.doutula.com/article/list/?page=%d'%(n)
        head={
            'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv: 65.0)Gecko/20100101Firefox/65.0'
        }
        qing=requests.get(url=ur,headers=head)
        html=qing.content.decode('utf-8')
        return html
    def guov(self,html):
        ab2=[]
        patt=re.compile('<a href="(.*?)" class="list-group-item random_list')
        patc=patt.findall(html)
        for i in range(len(patc)):
            ur=patc[i]
            head={
                'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv: 65.0)Gecko/20100101Firefox/65.0'
            }
            qingqiu2=requests.get(url=ur,headers=head)
            html2=qingqiu2.content.decode('utf-8')
            patt3=re.compile('this.src=\'(.*?)\'">',re.S)
            patc3=patt3.findall(html2)
            ab2.append(patc3)
        return ab2
    def baocun(self,abc):
        for i in range(len(abc)):
            for d in range(len(abc[i])):
                ll=abc[i][d].split('.')
                if  ll[-1]=='jpg':
                    res=requests.get(abc[i][d])
                    htm=res.content
                    with open(r'C:\Users\kong\Desktop\python学习\patu\%sm%s.jpg'%(i,d),'wb') as g:
                        g.write(htm)
                elif  ll[-1]=='gif':
                    res=requests.get(abc[i][d])
                    htm=res.content
                    with open(r'C:\Users\kong\Desktop\python学习\patu\%sm%s.gif'%(i,d),'wb') as g:
                        g.write(htm)
    def shnchu(self):
        all=os.listdir(r'C:\Users\kong\Desktop\python学习\patu')
        for h in range(len(all)):
            os.remove(r'C:\Users\kong\Desktop\python学习\patu\%s'%(all[h]))
a=doutu_Spider()
for s in range(1,3):
    html=a.qingqiu(s)
    abc=a.guov(html)
    a.baocun(abc)
