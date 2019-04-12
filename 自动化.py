#!/usr/bin/python
#-*- coding:utf-8 -*-
# 自动化测试脚本
#接口  对接口进行请求传参和结果对比
#http协议  requests  可以用来做http请求测试
#unitest  单元测试框架   主要是对用例进行管理和执行


# import json
# import requests
# import unittest
# import time
# import HTMLTestRunner
# class suopei(unittest.TestCase):
#
#     def  qingqiu(self):
#         url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
#         head = {
#             "Content-Type": "application/json",
#             "x-dealer-code": "2100150",
#             "x-position-code": "D_PO_1028",
#             "x-resource-code": "BASIC_DATA",
#             "x-track-code": "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#             "x-user-code": "djy0mx",
#             "x-access-token": "da05ee37e5676e7b27972b2892e0fdeb"
#         }
#         body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize":10,"curPage":1}'.encode(
#             'utf-8')
#         res = requests.post(url, headers=head, data=body)
#         js = res.json()
#         return js
#     def setUp(self):
#         print('天')
#     def test_1(self):
#         js=self.qingqiu()
#         self.assertEqual(js['data']['applicationType'][0]['name'],'多装')
#     def test_2(self):
#         js=self.qingqiu()
#         self.assertEqual(js['data']['applicationType'][0]['name'], '装')
#     def  test_3(self):
#         print('hello')
#     def  test_4(self):
#         print('mmm')
#
#     def  tearDown(self):
#         print('下')
# if  __name__=='__main__':
#     unittest.main()
# class suiyi(unittest.TestCase):
#     def  test_1(self):
#         self.assertEqual(10,10)
#     def test_2(self):
#         self.assertNotEqual(10,20)
#     def  test_3(self):
#         self.assertEqual(201,201)
#     def  test_4(self):
#         self.assertNotEqual(210,200)
# if __name__=='__main__':
#     ##########创建一个测试套件#######################
#     suit = unittest.TestSuite()                #创建一个测试套件
#     for i in range(1, 5):
#         suit.addTest(suiyi('test_{}'.format(i)))
#     now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
#     f = open('abc.html', 'wb')
#     runner = HTMLTestRunner.HTMLTestRunner(
#         stream=f, title='索赔测试报告', tester='Mr.kong', description='结果如下'
#     )
#     runner.run(suit)
#     f.close()





# url="https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
# head={
#     "Content-Type":"application/json",
#     "x-dealer-code":"2100150",
#     "x-position-code":"D_PO_1028",
#     "x-resource-code":"BASIC_DATA",
#     "x-track-code":"4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#     "x-user-code":"djy0mx",
#     "x-access-token":"da05ee37e5676e7b27972b2892e0fdeb"
# }
# body='{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize":10,"curPage":1}'.encode('utf-8')
# res=requests.post(url,headers=head,data=body)
# js=res.json()
# assert js['data']['applicationType'][0]['name']=='多装'
# assert js['data']['applicationType'][0]['value']=='1'
# class test_Spider(object):
#     pass


import json
import HTMLTestRunner
import requests
import unittest
import  time
class kuaicha(unittest.TestCase):

    def qingqiu(self):
        url="http://testsupport-be.haofenshu.com/v1/schools/infos?filterInput=北京"
        head={
            "Cookie":"yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN""zh""q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded"
        }
        res=requests.get(url,headers=head)
        js=res.json()
        return js
    def qingqiu2(self):
        url="http://testsupport-be.haofenshu.com/v1/schools/infos?filterInput=你"
        head={
            "Cookie":"yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN""zh""q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded"
        }
        res=requests.get(url,headers=head)
        js=res.json()
        return js
    def  test_school_quickly_check(self):
        js=self.qingqiu()
        self.assertEqual(js["code"],0)
        self.assertEqual(js["msg"],"学校快查成功")
        self.assertEqual(js["data"][0]["schoolName"],"北京中学")
        self.assertEqual(js["data"][0]["schoolId2.0"],"41467")
        self.assertEqual(js["data"][0]["address"],"北京朝阳")
    def test_school_quickly_check_2(self):
        js=self.qingqiu2()
        self.assertEqual(js["code"],1)
        self.assertEqual(js["msg"],"学校快查成功")
        self.assertEqual(js["data"],[])
if __name__=="__main__":
    suit=unittest.TestSuite()
    for i in range(1,3):
        suit.addTest(kuaicha('test_school_quickly_check_%d'%(i)))
    now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    with open('a.html','wb') as f :
        runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='快查测试报告',tester='mr.kong',description='结果如下')
        runner.run(suit)



