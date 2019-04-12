#!/usr/bin/python
#-*- coding:utf-8 -*-
# import unittest
# import time
# import HTMLTestRunner
# from 接口框架练习.test import test_suopei
# import json
#
# class suopei_baogao(unittest.TestCase):
#
#     def  test_1(self):
#         m=test_suopei.suopei_case()
#         return m.test_1()
#     def test_2(self):
#         n=test_suopei.suopei_case()
#         return n.test_2()
#     def test_3(self):
#         l=test_suopei.suopei_case()
#         return l.test_3()
# if __name__=='__main__':
#     suit=unittest.TestSuite()
#     for i in range(1,4):
#         suit.addTest(suopei_baogao('test_%s'%(i)))
#     now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#     with open('a.html','wb') as f:
#         runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='索赔测试报告',tester='Mr.kong',description='结果如下')
#         runner.run(suit)

import unittest
from   接口框架练习.report import HTMLTestRunner
from  接口框架练习.test import  *


def baogao_(aa):
    suit=unittest.TestSuite()
    #有两个参数，第一个参数为路径，第二个为正则，匹配条件
    #到这个路径下，匹配所有的以test开头的文件
    #test开头文件中找到函数以test开头
    for k in  aa:
        dis=unittest.defaultTestLoader.discover(r'C:\Users\kong\Desktop\python学习\接口框架练习\test',pattern='test_{}.py'.format(k.strip()))
        for i in dis:
            suit.addTest(i)
    f=open(r'C:\Users\kong\Desktop\python学习\接口框架练习\report\b.html','wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='测试索赔报告',tester='mr.kong',description='结果如下')
    runner.run(suit)
    f.close()
if  __name__=='__main__':
    baogao_()