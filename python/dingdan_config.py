#!/usr/bin/python
#-*- coding:utf-8 -*-
import  requests
import json

class Dingdan(object):

    def shouye_zhuangtai(self):
        url='https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderHomePage'
        head={
            'Content - Type': 'application / json',
            'x - dealer - code': 2100005,
            'x - position - code': 'D_PO_1028',
            'x - resource - code': 'pol4s_partOrder_orderHomePage',
            'x - track - code': '4320e7d0 - cf0c - 7ba2 - b3fe - 1ecb1f15e394',
            'x - user - code':'dhxc1u',
            'x - access - token': 'da05ee37e5676e7b27972b2892e0fdeb'
        }
        res=requests.post(url,headers=head)
        return res.json()
    def chauxun_dingdan(self,a,b,c,d,e,f,g,h):
        url='https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderList'
        head= {
            'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_orderList",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "da05ee37e5676e7b27972b2892e0fdeb",
            'cache-control': "no-cache",
            'Postman-Token': "c9b209e2-eab7-4aca-88e5-4042e2499e84"
        }

        body='{"pageNum": %s,"pageSize": %s,"queryTerms": {"orderType": %s,"orderStatus": %s,"orderDelayFlag": %s,"orderNo": %s,"startReportDate": %s,"endReportDate": %s}'%(a,b,c,d,e,f,g,h)
        body=body.encode('utf-8')
        res=requests.post(url=url,headers=head,data=body)
        print(res.json())
    def yanqi_quxiao(self,a,b):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/delayOrderCancelStatus/getCancelDelayOrder'
        head={
            'Content-Type': 'application/json',
            'x-dealer-code': '2100005',
            'x-position-code':'D_PO_1028',
            'x-resource-code':'pol4s_delayOrderCancelStatus_getCancelDelayOrder',
            'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
            'x-user-code':'dhxc1u',
            'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb'
        }
        body="{\r\n \"pageNum\":%s,\r\n \"pageSize\": %s,\r\n \"queryTerms\": {\r\n    \"orderNo\":\"R2100654\",\r\n    \"cancelStatus\":-1,\r\n    \"applyStartDate\":20180801,\r\n    \"applyEndDate\":20180909\r\n }\r\n}"%(a,b)
        res=requests.post(url,headers=head,data=body)
        js=res.json()
        return js
    def dingdan_mingxi(self,a,b,c):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch'
        head= {
            'Content-Type': "application/json",
            'x-dealer-code': "2100005",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrderSearch_partOrderDetailSearch",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "da05ee37e5676e7b27972b2892e0fdeb",
            'cache-control': "no-cache",
            'Postman-Token': "584b324a-ddf0-4221-9966-76a193a586d5"
        }
        body="{\r\n \"pageNum\":%s,\r\n \"pageSize\":%s,\r\n \"queryTerms\":\r\n {\r\n  \"orderNo\":%s\r\n }\r\n}"%(a,b,c)
        body=body.encode('utf-8')
        res=requests.post(url,headers=head,data=body)
        js=res.json()
        return js
    def peijian_mingxi(self,a):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderPartDetail'
        head= {
            'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_orderPartDetail",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "da05ee37e5676e7b27972b2892e0fdeb",
            'cache-control': "no-cache",
            'Postman-Token': "6b2e35c6-0b44-4071-bef5-90290ff276d8"
        }
        body="{\r\n \"partOrderItemId\":%s\r\n}"%(a)
        body=body.encode('utf-8')
        res=requests.post(url,headers=head,data=body)
        js=res.json()
        return js

