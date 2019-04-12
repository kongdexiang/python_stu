#!/usr/bin/python
#-*- coding:utf-8 -*-
import  xlrd
class xuexiao_duqu(object):
    def suozaidi(self):
        diqu=[]
        f=xlrd.open_workbook(r'C:\Users\kong\Desktop\python学习\接口框架练习\data\xuexiaodiqu.xlsx')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for i in range(num):
            if i ==0:
                continue
            else:
                diqu.append(sheet.row_values(i))
        return diqu

if __name__=='__main__':
    a=xuexiao_duqu()
    a.suozaidi()