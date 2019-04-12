#!/usr/bin/python
#-*- coding:utf-8 -*-
import  unittest
import requests
from  接口框架练习.config import  xuexiaochaxun
from  接口框架练习.data import  xuexiao_duqu

class xuexiao_Case(unittest.TestCase):
    diqu=xuexiao_duqu.xuexiao_duqu()
    canshu=diqu.suozaidi()

    def  test_school_quickly_check(self):
        xue = xuexiaochaxun.Xuexiao()
        eg=xue.xuexiao_chaxun(self.canshu[0][0])
        self.assertEqual(eg["code"], 0)
        self.assertEqual(eg["msg"], "学校快查成功")
    def  test_school_quickly_check2(self):
        xue = xuexiaochaxun.Xuexiao()
        eg=xue.xuexiao_chaxun(self.canshu[1][0])
        self.assertEqual(eg["code"], 0)
        self.assertEqual(eg["msg"], "学校快查成功")
    def   test_school_quickly_check3(self):
        xue = xuexiaochaxun.Xuexiao()
        eg = xue.xuexiao_chaxun(self.canshu[2][0])
        self.assertEqual(eg["code"], 1)
        self.assertEqual(eg["msg"], "学校快查成功")
    def test_school_quickly_check4(self):
        xue = xuexiaochaxun.Xuexiao()
        eg = xue.xuexiao_chaxun(self.canshu[3][0])
        self.assertEqual(eg["code"], 1)
        self.assertEqual(eg["msg"], "学校快查成功")
    def test_school_quickly_check5(self):
        xue = xuexiaochaxun.Xuexiao()
        eg = xue.xuexiao_chaxun(self.canshu[4][0])
        self.assertEqual(eg["code"], 1)
        self.assertEqual(eg["msg"], "学校快查成功")
