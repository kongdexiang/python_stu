#!/usr/bin/python
#-*- coding:utf-8 -*-
import xlrd


class Dingdan(object):

    def chaxun_shuju(self):
        chaxun = []
        f = xlrd.open_workbook(r'C:\Users\kong\Desktop\python学习\接口框架练习\data\dingdan_chaxundingdan.xlsx')
        sheet = f.sheets()[0]
        aa = sheet.nrows
        for i in range(aa):
            if i == 0:
                continue
            else:
                chaxun.append(sheet.row_values(i))
        return chaxun
    def yanqi_dingdan(self):
        yanqi=[]
        f=xlrd.open_workbook(r'C:\Users\kong\Desktop\python学习\接口框架练习\data\dingdan_quxiaoyanqidingdan.xlsx')
        sheet=f.sheets()[0]
        ac=sheet.nrows
        for j in range(ac):
            if j ==0:
                continue
            else:
                yanqi.append(sheet.row_values(j))
        return yanqi
    def dingdan_mingxi(self):
        mingxi=[]
        f=xlrd.open_workbook(r'C:\Users\kong\Desktop\软件测试\接口测试\接口测试实践\别克测试用例\订单明细\订单明细变量.xlsx')
        sheet=f.sheets()[0]
        mx=sheet.nrows
        for i in range(mx):
            if i == 0:
                continue
            else:
                mingxi.append(sheet.row_values(i))
        return mingxi
    def peijian_mingxi(self):
        peijian=[]
        f=xlrd.open_workbook(r'C:\Users\kong\Desktop\python学习\接口框架练习\data\dingdan_peijianmingxi.xlsx')
        sheet=f.sheets()[0]
        ab=sheet.nrows
        for i in range(ab):
            if i == 0:
                continue
            else:
                peijian.append(sheet.row_values(i))
        return peijian
