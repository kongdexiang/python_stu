#!/usr/bin/python
#-*- coding:utf-8 -*-
import unittest
from 接口框架练习.report import HTMLTestRunner
from 接口框架练习.test import  *

def  Xuexiao_baogao(cc):
    suit=unittest.TestSuite()
    for k in cc:
        dis=unittest.defaultTestLoader.discover(r'C:\Users\kong\Desktop\python学习\接口框架练习\test',pattern='{}_test.py'.format(k.strip()))
        for i in dis:
            suit.addTest(i)
    f=open(r'C:\Users\kong\Desktop\python学习\接口框架练习\report\a.html','wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='学校查询测试报告',tester='Mr.kong',description='结果如下')
    runner.run(suit)
    f.close()
if __name__ =='__main__':
    Xuexiao_baogao()