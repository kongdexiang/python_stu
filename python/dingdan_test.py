#!/usr/bin/python
#-*- coding:utf-8 -*-

import unittest
from 接口框架练习.config import dingdan_config
from 接口框架练习.data import  dingdan_shuju
import requests

class shouye_zhuangtai_Case(unittest.TestCase):


    def  test_zhuangtai(self):
        ts=dingdan_config.Dingdan()
        eg=ts.shouye_zhuangtai()
        self.assertEqual(eg.status,1)
        self.assertEqual(eg.errMsg,'处理成功')


class dingdan_chaxun(unittest.TestCase):
    shu = dingdan_shuju.Dingdan()
    shuju = shu.chaxun_shuju()

    def test_valid(self):
        ts = dingdan_config.Dingdan()
        eg = ts.chauxun_dingdan(int(self.shuju[0][0]), int(self.shuju[0][1]), int(self.shuju[0][2]),int(self.shuju[0][3]),self.shuju[0][4],self.shuju[0][5],self.shuju[0][6],self.shuju[0][7])
        self.assertEqual(eg.status, 1)
        self.assertEqual(eg.errMsg, '处理成功')
    def test_valid2(self):
        ts = dingdan_config.Dingdan
        eg = ts.chauxun_dingdan(int(self.shuju[1][0]), int(self.shuju[1][1]), int(self.shuju[1][2]), int(self.shuju[1][3]),int(self.shuju[1][4]), self.shuju[1][5], self.shuju[1][6], self.shuju[1][7])
        self.assertEqual(eg.status, 1)
        self.assertEqual(eg.errMsg, '处理成功')


class  yanqi_dingdan_case(unittest.TestCase):

    cs=dingdan_shuju.Dingdan()
    dt=cs.yanqi_dingdan()
    def  test_val1(self):
        ds=dingdan_config.Dingdan()
        da=ds.yanqi_quxiao(int(self.dt[0][0]),int(self.dt[0][1]))
        self.assertEqual(da.status,1)
        self.assertEqual(da.data.pageNum,int(self.dt[0][0]))
    def  test_val2(self):
        ds=dingdan_config.Dingdan()
        da=ds.yanqi_quxiao(self.dt[1][0],int(self.dt[1][1]))
        self.asserEqual(da.message,'get error')
    def test_val3(self):
        ds=dingdan_config.Dingdan()
        da=ds.yanqi_quxiao(self.dt[2][0],int(self.dt[2][1]))

class  Dingdan_Mingx(unittest.TestCase):
    shu=dingdan_shuju.Dingdan()
    mingx=shu.dingdan_mingxi()

    def test_valmx1(self):
        dc=dingdan_config.Dingdan()
        ds=dc.dingdan_mingxi(int(self.mingx[0][0]),int(self.mingx[0][1]),self.mingx[0][2])
        self.assertEqual(ds.status,1)
    def test_valmx2(self):
        dc=dingdan_config.Dingdan()
        ds=dc.dingdan_mingxi(self.mingx[1][0],int(self.mingx[1][1]),self.mingx[1][2])
        self.assertEqual(ds.status,0)

class Peijian_mingxi(unittest.TestCase):
    shu=dingdan_shuju.Dingdan()
    pj=shu.peijian_mingxi()

    def test_valpj(self):
        ds=dingdan_config.Dingdan()
        dc=ds.peijian_mingxi(int(self.pj[0][0]))
        self.assertEqual(dc.status,1)

    def test_valpj2(self):
        ds = dingdan_config.Dingdan()
        dc = ds.peijian_mingxi(int(self.pj[0][1]))
        self.assertEqual(dc.status,0)
# if __name__=='__main__':
#     unittest.main()
# yanqi_dingdan_case().test_val1()