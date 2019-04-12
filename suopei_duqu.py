#!/usr/bin/python
#-*- coding:utf-8 -*-
import xlrd

class Suopei_duqu(object):

    def duqu_jichu(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\kong\Desktop\python学习\接口框架练习\data\suopei.xls')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for i in range(num):
            if  i==0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju
if  __name__=='__main__':
    s=Suopei_duqu()
    s.duqu_jichu()
