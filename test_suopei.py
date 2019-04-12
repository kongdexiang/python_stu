#!/usr/bin/python
#-*- coding:utf-8 -*-
import unittest
import requests
from 接口框架练习.config import  suopei
from 接口框架练习.data import  suopei_duqu
class suopei_case(unittest.TestCase):
    jichu = suopei_duqu.Suopei_duqu()
    canshu = jichu.duqu_jichu()
    def test_1(self):
        suo=suopei.Suopei()
        asd=suo.jichu_shuju(int(self.canshu[0][0]),int(self.canshu[0][1]))
        self.assertEqual(asd['data']['applicationType'][0]['name'],'多装')
    def  test_2(self):
        suo = suopei.Suopei()
        asd = suo.jichu_shuju(self.canshu[1][0], int(self.canshu[1][1]))
        self.assertEqual(asd['message'],"get error")
    def test_3(self):
        suo = suopei.Suopei()
        asd = suo.jichu_shuju(int(self.canshu[2][0]), self.canshu[2][1])
        self.assertEqual(asd['message'],"get error")