#!/usr/bin/python
#-*- coding:utf-8 -*-
#########     #############
#client  客户端
import socket
#创建套接字
# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #连接服务器     接收的是元组
# sock.connect(('127.0.0.1',8888))    #ip地址是服务器的ip地址
# #发送请求 send
# reg=input('>>>>')
# sock.send(reg.encode('utf-8'))
# #接受数据
# msg=sock.recv(1024)
# print(msg.decode('utf-8'))
# #断开连接
# sock.close()


# while True:
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect(('127.0.0.1', 8888))
#     reg=input('>>>>>')
#     if reg=='exit':
#         sock.close()
#         break
#     else:
#         sock.send(reg.encode('utf-8'))
#         msg=sock.recv(1024)
#         print(msg.decode('utf-8'))

import socket
while True:
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#发送请求
    host=('127.0.0.1',8888)
    asr=input('请求内容>>>')
    if asr=='exit':
        break
    else:
        sock.sendto(asr.encode('utf-8'),host)
#接收数据
        msg=sock.recv(1024)
        print(msg.decode('utf-8'))
sock.close()

