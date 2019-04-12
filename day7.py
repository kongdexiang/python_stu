#!/usr/bin/python
#-*- coding:utf-8 -*-
from time import sleep
# import threading
# def asd():
#     for i in range(3):
#         print('打篮球')
#         sleep(4)
# def asr():
#     for j  in range(3):
#         print('送饮料')
#         sleep(2)
# threading.Thread(target=asd).start()   #.start 是开启线程
# threading.Thread(target=asr).start()



import time
#时间戳，从公元1970年到现在所经过的秒数
# bb=time.time()
# print(bb)
# print(time.localtime())
# abc=time.localtime()
# # print(time.strftime('%Y-%m-%d %H:%M:%S %a %j'))
#格局现代化的时间，格式化成元祖
# ab=time.strptime('1993-01-02','%Y-%m-%d') #括号内前后格式要一致
#将元祖类型的时间变成时间戳
# print(time.mktime(ab))

# 输入一个日期，打印是否是闰年 ， 星期几，一年中的第几天
# def panduan():
#     a=input('输入一个日期,格式为(%Y-%m-%d)》》》》》》')
#     ab=time.strptime(a,'%Y-%m-%d')
#     if ab[0]%4==0:
#         if ab[0]%400==0:
#             print('%s年是世纪闰年'%(ab[0]))
#         else:
#             print('%s年是闰年'%(ab[0]))
#     else:
#         print('%s年不是闰年'%(ab[0]))
#     print('今天是星期%s' % (ab[6]))
#     print('今天是一年中的第%s天' % (ab[7]))
# panduan()

# #######################用python发送邮件#######################
# import smtplib   #连接邮件服务器
# import email.mime.multipart   #处理邮件的组成
# import email.mime.text    #处理邮件正文
# import xlrd
#
# server='smtp.163.com'   #邮件服务器
# from_user='18236549823@163.com'
# res= '1258153711@qq.com'
# passwd='kongdexiang123'    #授权码   允许登陆客户端的密码
#
# ####创建一个空的邮件
# message=email.mime.multipart.MIMEMultipart()
# ####邮件的发件人#
# message['from']=from_user
# ###邮件的接受者
# message['To']=res
# ######邮件的主题
# message['subject']='python learn'
# ####邮件的内容
# text= """
# 中国，你好，while来自外太空
# 希望你不要令我失望
# """
# ######对正文进行编码
# text=email.mime.text.MIMEText(text,'plain','utf-8')
# #######带附件的邮件需要添加以下代码
#
# #####将正文添加到邮件中
# message.attach(text)
# #######对附件进行读取进行编码
# att2=email.mime.text.MIMEText(open('htm.txt','rb').read(),'base64','utf-8')
# ####给附件添加头部信息
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"]='attachment;filename="htm.txt"'
# message.attach(att2)
# ####连接服务器
# smtp123=smtplib.SMTP_SSL(server,465)
# #####登陆服务器
# smtp123.login(from_user,passwd)
# #####发送邮件
# smtp123.sendmail(from_user,res,message.as_string())
# #######断开连接
# smtp123.close()


##########
# import paramiko
#首先创建一个远程客户端 用来连接linux
# sss=paramiko.SSHClient()
#第一次连接主机，known hosts 存放的是主机地址，需要跳过查找
# sss.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# #连接主机
# sss.connect(hostname='192.168.0.95',
#             port=22,
#             username='root',
#             password='123456')
#输入命令需要三个变量
#exec_command 括号里面是执行命令，  括号里面必须是有直接结果的命令
# a,b,c=sss.exec_command('ls -al /etc')
#第一个变量表示的是输入的命令
# 第二个变量表示的是命令执行的结果
# 第三个变量 表示的是命令的报错
# print(b.read().decode())       #读出命令的结果
#断开连接
# sss.close()

# ###################可以无限输入linux命令#############输入exit结束
# import paramiko
# with paramiko.SSHClient() as sss:
#     sss.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#     sss.connect(hostname='192.168.0.95',
#                 port=22,
#                 username='root',
#                 password='123456')
#     while True:
#         aa = input('输入linux直接有结果的命令》》》》')
#         try:
#
#             if aa=='exit':
#                 break
#             else:
#                 a,b,c=sss.exec_command('%s'%(aa))
#                 print(b.read().decode())
#         except:
#             print('输入命令错误，请重新输入')
#             continue
# #
# import paramiko
# #传输文件
# #建立一个传输通道
# sss=paramiko.Transport('192.168.0.95',22)
# #连接linux
# sss.connect(username='root',password='123456')
# #创建一个传输文件的对象
# sftp=paramiko.SFTPClient.from_transport(sss)
# #从linux上面到windows上面传文件
# #第一个参数表示要传输的文件
# #第二个参数表示存放的本机位置
# # sftp.get('install.log',r'.\abc.log')         #注  get是下载   put是上传
# #从windows到linux传输文件
# #第一个参数表示要传输的文件
# #第二个便是存放到linux问文件的位置
# sftp.put('ab.txt','/home/ab.txt')
# sss.close()


########################## socket##############
#python自带的模块
# 介绍：套接字，是实现最底层的一种通信方式  ：接收功能和发送功能
#采用的是cs架构

#实现通过tcp协议来通信

#server 端  服务器端
import socket

#创建一个套接字（创建一个有接收和发送能力的） 并且规定使用tcp协议，规定使用ip的版本为ipv4
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定ip地址和端口号  bind接收的是一个元组
s.bind(('0.0.0.0',8888))    #里面是一个元组
#监听服务是否开启,数字指的是最大等待数
s.listen(3)
while True:
    #接收请求 会产生两个数值，第一个变量名表示 连接信息  第二个变量表示 客户端的ip地址和端口号
    conn,addr=s.accept()
    #接收数据  1024  表示一次性最大能接收1024字节的数据
    reg=conn.recv(1024)
    reg2=reg.decode('utf-8')   #decode :解码
    if reg2=='exit':
        continue
    else:
    #发送数据
        msg=input('>>>>')
        conn.send(msg.encode('utf-8'))