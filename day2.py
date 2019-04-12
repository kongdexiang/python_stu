#!/usr/bin/python
# -*- coding:utf-8 -*-
# class asd():
#     def 天下(self):
#         asd().你好()
#         print('天下是我的')
#     def  我的(self):
#         tian.你好()
#         print('我的天下')
#     def __你好(self):
#         print('hello')
# 小新=asd()
# # class new_asd(asd):         #一个新的类可以继承旧的类中的所有函数
# #     pass
# class new_asd:
#     def 素数之和(self):
#         print('1060')
# class bu_asd:
#     def 你好(self):
#         print('......')
# class xin_asd(new_asd,asd,bu_asd):        #一个新的类可以同时继承多个旧的类的所有函数
#     pass
# xin_asd().你好()                 #注：新的类继承多个旧的类的时，如果旧的类中有相同的函数，则先继承哪一个类，用那一个类的方法
################类的属性##############################
# class asr():                                   #初始化属性，让属性成为可以变化的
#     def __init__(self,x,y):
#         self.name=x
#         self.age=y
#     def 对话(self):
#         print('你今年多大了？ %s'%(self.name))
#     def 聊天(self):
#         print('我今年%d岁'%(self.age))
# ad=asr('小明',20)
# ad.对话()
# ad.聊天()

# import re
# with open('c.txt','r+',encoding='utf=8') as  f:
#     a=f.read()
#     b=[]
#     aa=re.compile('.*a.*')
#     ab=re.compile('.*b.*')
#     ac=re.compile('.*c.*')
#     for i in a :
#         if aa.findall(i) in i or ab.findall(i) in i or ac.findall(i) in i:
#             b.append(i)

import requests
ur={
	{GET http://v.gdt.qq.com/gdt_stats.fcg?viewid=8dyacVItdXg!KTEhLx48X41iUiiNl77mgvERBiVIrleO48xw5FwTJ996pKGnaKBZM_uPsaMhq!JoZc3rbfaI2tQwuFj0zproVCgsv8A7fQ0BSyQr8m3KdaxuaeOmG2W_dWRgWhmS1zHtBfP0dPQQC!jhedGWnJL3&i=1&os=0&xp=2 HTTP/1.1
Host: v.gdt.qq.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0
Accept: image/webp,*/*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: keep-alive
Cookie: _qpsvr_localtk=0.8917830262012543; pgv_pvi=9063916544; pgv_si=s9481380864; pgv_pvid=27414272; pgv_info=ssid=s5538758890; ptisp=cnc; ptui_loginuin=2215881363; uin=o2215881363; skey=@01mrpgbyj; RK=QRo13PyY1C; ptcz=3ffd0b80f0c1cc45db860c9562687a9b192b4584acf547e6bc9ab46d4ead102b

}
}