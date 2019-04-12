#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import json

class Suopei(object):

    def jichu_shuju(self,a,b):
        url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
        head = {
            "Content-Type": "application/json",
            "x-dealer-code": "2100150",
            "x-position-code": "D_PO_1028",
            "x-resource-code": "BASIC_DATA",
            "x-track-code": "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            "x-user-code": "djy0mx",
            "x-access-token": "da05ee37e5676e7b27972b2892e0fdeb"
        }
        body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize":%s,"curPage":%s}'%(a,b)
        body=body.encode('utf-8')
        res = requests.post(url, headers=head, data=body)
        js = res.json()
        return js

if  __name__=='__main__':
    ss=Suopei()
    bb=ss.jichu_shuju(a=10,b=1)
    print(bb)
