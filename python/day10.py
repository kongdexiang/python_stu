#!/usr/bin/python
#-*- coding:utf-8 -*-
#####99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d'%(i,j,i*j),end='\t')
#     print('')

#udp 实现通信
import  socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定主机
s.bind(('127.0.0.1',8888))
#不需要监听
while True:
    #第一个变量为客户端发送的请求数据，第二个为客户端的ip和端口号
    conn,addr=s.recvfrom(1024)
    #打印接收到的数据
    asr=conn.decode('utf-8')
    if asr=='exit':
        print(asr)
        continue
    #发送响应
    else:
        print(asr)
        asd=input('>>>')
        s.sendto(asd.encode('utf-8'),addr)  #前面为server 响应的数据   后面是addr

