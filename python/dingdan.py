#!/usr/bin/python
#-*- coding:utf-8 -*-
from 接口框架练习.report.dingdan_report  import  dingdan_baogao

def run(aa):
    dingdan_baogao(aa)
with open(r'C:\Users\kong\Desktop\python学习\接口框架练习\driver\shouye.txt','r+') as f:
    bb=f.readlines()
    if len(bb)==1:
        run('dingdan')
    else:
        run('bb')