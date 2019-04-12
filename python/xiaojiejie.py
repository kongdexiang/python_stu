#!/usr/bin/python
#-*- coding:utf-8 -*-


from tkinter import *
from tkinter import messagebox    #消息提示模块
from PIL import Image
from PIL import  ImageTk          #处理图片的

#自带的模块  图形模块
def closewindows():
    #设置提示信息
    messagebox.showinfo(title='哈哈哈',message='就是关不掉')
    #关闭窗口
    windows.destroy()
    return
def love():
    #创建一个顶级窗口，依赖于原始的窗口存在
    love=Toplevel(windows)
    love.geometry('300x100+600+400')
    love.title('明智的选择')
    lable2=Label(love,text='好巧,我也是！！！',font=('宋体',20))
    lable2.grid(row=4,column=3)
    bot=Button(love,text='确定',font=('宋体',20))
    bot.grid(row=6,column=3)
    love.mainloop()
def nolove():
    pass
####创建一个窗口#############
windows=Tk()
########更改窗口的标题################
windows.title('小姐姐，选择哦！！！')
####设置窗口的大小####
windows.geometry('1000x800')
#######设置窗口的位置#########
windows.geometry('+400+0')
#########当用户关闭窗口时触发
windows.protocol('WM_DELETE_WINDOW',closewindows)
#########添加文本标签################
label=Label(windows,text='hello!!! 小姐姐',font=('正楷',20))
#########显示标签#############   N W E S 东 南 西 北
label.grid(row=0,column=0,sticky=W)   # row  为行 column 为列     sticky 为
######添加图片控件########
# imag=PhotoImage(file=r'C:\Users\kong\Desktop\python学习\patu\2m4.gif')
# image=Label(windows,image=imag)
# image.grid(row=2,columnspan=2)
######第二种方法添加图片控件
photo=Image.open(r'C:\Users\kong\Desktop\python学习\patu\2m4.jpg')
ptot=ImageTk.PhotoImage(photo)
phto=Label(windows,image=ptot)
#####显示数据
phto.grid(row=2,columnspan=2)
#######添加一个按钮控件##########
botten=Button(windows,text='同意',width=10,height=3,command=love)
botten.grid(row=5,column=0,sticky=W)
#####添加另一个按钮控件###########
botten1=Button(windows,text='不同意',width=10,height=3,command=nolove)
botten1.grid(row=5,column=0,sticky=E)
#####显示窗口###########
windows.mainloop()
#######