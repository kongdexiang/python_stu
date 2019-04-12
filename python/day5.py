#!/usr/bin/python
#-*- coding:utf-8 -*-
#############json模块####################
# import  json
#主要用在web端发送数据的
# json 是在javascript里面的一种数据类型  在javascript 中叫json
#做动态网页爬虫的时候会用到json
#json.dumps() :   将字典变成json数据
#json.loads() : 　　将ｊｓｏｎ

# #################爬取智联招聘##########
import re
import requests
import xlrd
import xlwt
import xlutils
from xlutils.copy import copy
class  zhilian_Spider(object):
    m=input('输入职位>>>>')
    d=input('输入地址编号>>>')
    def qingqiu(self,mz=m,dizhi=d,p90=90):
        ur='https://fe-api.zhaopin.com/c/i/sou?start=%s&pageSize=%s&cityId=%s&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%s&kt=3&_v=0.03553700&x-zp-page-request-id=1876495414324430901d522ec955540e-1550653002616-368922'%(p90,dizhi,mz)
        head={
            'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:65.0)Gecko/20100101Firefox/65.0'
        }
        qing=requests.get(url=ur,headers=head)
        html=qing.content.decode('utf-8')
        return html
    def fenxi(self,html):
        gongsi=[]
        zhiwei=[]
        gongzuojingyan=[]
        gongzi=[]
        fuli=[]
        dizhi=[]
        zd=json.loads(html)
        for i in range(90):
            gs=zd['data']['results'][i]['company']['name']
            gongsi.append(gs)
        for j in range(90):
            zw=zd['data']['results'][j]['jobName']
            zhiwei.append(zw)
        for w in range(90):
            jingy=zd['data']['results'][w]['workingExp']['name']
            gongzuojingyan.append(jingy)
        for e in range(90):
            gz=zd['data']['results'][e]['salary']
            gongzi.append(gz)
        for r in range(90):
            fl=zd['data']['results'][r]['welfare']
            fuli.append(fl)
        for t in range(90):
            di=zd['data']['results'][t]['city']['display']
            dizhi.append(di)
        return gongsi,zhiwei,gongzuojingyan,gongzi,fuli,dizhi
    def baocun(self,xinxi):
        f=xlrd.open_workbook('招聘信息.xls')
        new_f=copy(f)
        sheet=new_f.get_sheet(0)
        for y in range(len(xinxi)):
            for u,o in enumerate(xinxi[y]):
                sheet.write(u+1,y,o)
        new_f.save('招聘信息.xls')
xin=xlwt.Workbook('utf-8')
sheet=xin.add_sheet('公司信息')
sheet.write(0,0,'公司名称')
sheet.write(0,1,'招聘职位')
sheet.write(0,2,'工作经验')
sheet.write(0,3,'工资')
sheet.write(0,4,'员工福利')
sheet.write(0,5,'公司地址')
xin.save('招聘信息.xls')
a=zhilian_Spider()
html=a.qingqiu()
xinxi=a.fenxi(html)
a.baocun(xinxi)



# json='https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=12&city=410200&geoobj=114.204118|34.717507|114.588639|34.882148&keywords=鸡公煲'
# jonn='https://fe-api.zhaopin.com/c/i/sou/?start=90&&page-title?start=0&pageSize=90&cityId=530&areaId=&businessarea={}&industry=&salary=&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&jobType=-1&sortType=&kw=测试工程师&kt=3&bj=&sj=&lastUrlQuery={"jl":"530","kw":"测试工程师","kt":"3"}&companyNo=&companyName=&_v=0.06496989&x-zp-page-request-id=77513af281c9447ca18e3a895a64c856-1550647869349-887618'
# jonn1='https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=测试工程师&kt=3&_v=0.06496989&x-zp-page-request-id=77513af281c9447ca18e3a895a64c856-1550647869349-887618'