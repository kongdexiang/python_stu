#!/usr/bin/python
#-*- coding:utf-8 -*-
from 接口框架练习.report import  HTMLTestRunner
from 接口框架练习.test import dingdan_test
import  unittest


def  dingdan_baogao(dd):
    suit=unittest.TestSuite()
    for i in  dd:
        dis=unittest.defaultTestLoader.discover(r'C:\Users\kong\Desktop\python学习\接口框架练习\test',pattern='{}_test.py'.format(i.strip()))
        for k in dis:
            suit.addTest(k)
        f=open(r'C:\Users\kong\Desktop\python学习\接口框架练习\report\shouye.html','wb')
        runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='订单测试报告',tester='Mr.kong',description='结果如下')
        runner.run(suit)
        f.close()
