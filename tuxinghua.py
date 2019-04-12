#!/usr/bin/python
#-*- coding:utf-8 -*-
#Author: 白志强
#@Time: 2018/7/13 16:41

from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk


def closeWindow():
    # 设置提示信息
    messagebox.showinfo(title='警告', message='不许关闭,好好回答')
    return

# 点击同意


def Love():
    # 顶级窗口 在原窗口之上又创建了个
    love = Toplevel(window)
    love.geometry("300x100+520+260")
    love.title("好巧，我也是")
    label = Label(love, text="好巧，我也是", font=("微软雅黑", 20))
    label.grid()
    # entry = Entry(love,font=('微软雅黑',18))
    # entry.pack()
    btn = Button(love, text="确定", width=10, height=2, command=closeallwindow)
    btn.pack()
    love.protocol('WM_DELETE_WINDOW', closelove)


def closelove():
    # return

    messagebox.showinfo(title='哈哈哈', message='刚好，我也是')
    return
# 关闭所有窗口


def closeallwindow():
    # 销毁所有窗口
    window.destroy()
    # messagebox.showinfo(title='哈哈哈',message='还是关不掉')
    # return


def NoLove():
    no_love = Toplevel(window)
    no_love.geometry("300x100+520+260")
    no_love.title("再考虑考虑")
    label = Label(no_love, text="想清楚再说", font=("微软雅黑", 20))
    label.pack()
    btn = Button(no_love, text="好的", width=10,
                 height=2, command=no_love.destroy)
    btn.pack()
    no_love.protocol('WM_DELETE_WINDOW', closenolove)


def closenolove():
    # messagebox.showinfo(title='再考虑一下', message='再考虑考虑')
    # return
    NoLove()


# 创建窗口
window = Tk()
# 窗口标题
window.title("你喜欢我吗？")
# 设置窗口大小  中间用小写x
window.geometry("380x420+500+240")
# 设置窗口位置   几何  根据右上角位置来的
# window.geometry("+520+240")
# 用户关闭窗口触发的时间
window.protocol('WM_DELETE_WINDOW', closeWindow)
#标签对象  (控件)
label = Label(window, text='hey,小姐姐', font=("微软雅黑", 15))
# text 窗口文本  font 设置字体   fg设置字体颜色
# 控件的位置  pack 包
label.grid(row=0, column=0)  # 网格布局
label1 = Label(window, text="喜欢我吗？", font=("微软雅黑", 30))

# row 行  column列  sticky对齐方式 N S W E
label1.grid(row=1, column=1, sticky=E)
# 显示图片
# photo = PhotoImage(file='cc.png')

# imagelabel = Label(window, image=photo)
# # columnspan 组件所跨越的列数
# imagelabel.grid(row=2, columnspan=2)
img = Image.open('cc.png')
photo = ImageTk.PhotoImage(img)
imgphoto = Label(window, image=photo)
imgphoto.grid(row=2, columnspan=2)

# 按钮组件  ## width 宽度  height高度
btn = Button(window, text="喜欢", width=15, height=2, command=Love)
btn.grid(row=3, column=0, sticky=W)

btn1 = Button(window, text="不喜欢", command=NoLove)
btn1.grid(row=3, column=1, sticky=E)
# 显示窗口，，，，消息循环
window.mainloop()

