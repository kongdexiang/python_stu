#!/usr/bin/python
#-*- coding:utf-8 -*-
from 接口框架练习.report.xuexiao_baogao import Xuexiao_baogao

def run(cc):
    Xuexiao_baogao(cc)

with open(r'C:\Users\kong\Desktop\python学习\接口框架练习\driver\xuexiao.txt','r') as f:
    a=f.readlines()
    if len(a)==1:
        run('*')
    else:
        run(a)
