#!/usr/bin/python
#-*- coding:utf-8 -*-
# from selenium import  webdriver
# from time import sleep
#########定义使用什么浏览器###########
# dr=webdriver.Firefox()
# ######设置浏览器的大小
# # dr.set_window_size(400,400)
# # sleep(2)
# #####打开网址#######
# dr.get('https://www.baidu.com')
# sleep(2)
#####定位###
# #1.通过id来定位
# dr.find_element_by_id('kw').send_keys(23134)
# sleep(2)
# dr.find_element_by_id('su').click()
# sleep(2)
#2.通过class_name来定位   是通过标签的class属性来定位
# dr.find_element_by_class_name('s_ipt').send_keys(112132)
# sleep(2)
# dr.find_element_by_class_name('bg s_btn').click()
# sleep(2)
#3.通过标签上的name定位
# dr.find_element_by_name('wd').send_keys(21367)
# sleep(2)
# dr.find_element_by_id('su').click()
# sleep(2)
#4.通过link text来定位  标签的文本定位
# dr.find_element_by_link_text('hao123').click()
#5.通过标签的模糊文本来定位 partial link text
# dr.find_element_by_partial_link_text('hao').click()
#6.通过标签名称来定位    tag_name   是最不唯一的一个定位 ，通常用来定位一组数据
# dr.find_elements_by_tag_name()
#7.css_selector 定位  通过css来定位
# dr.find_element_by_css_selector()
#8.xpath 定位，
#xpath  路径标记语言
#xml   可扩展性标记语言
# dr.find_element_by_xpath('//*[@id="kw"]').send_keys(738498732)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="su"]').click()
# sleep(2)
#优先级 ：  id > css > xpath > name > class_name > link text > partial link text
########获取网址的标题#########

# print(dr.title)
####获取打开网页的网址
# print(dr.current_url)
# dr.get('https://www.jd.com')
# sleep(2)
# #####回退
# dr.back()
# sleep(2)
# ########前进######
# dr.forward()
# sleep(2)
#####设置浏览器的位置
# dr.set_window_position(450,250)
# sleep(2)
# #设置浏览器窗口最大化
# dr.maximize_window()
# sleep(2)
# #设置浏览器窗口最小化
# dr.minimize_window()
# sleep(2)
#########关闭网页#####
# dr.quit()

# from selenium import  webdriver
from time import  sleep
# dr=webdriver.Firefox()
# dr.get('https://qzone.qq.com')
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys(1258153711)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('special1314...')
# sleep(2)
# dr.find_element_by_id('login_button').click()
# sleep(5)
# dr.quit()
# dr.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
#定位一组对象  对多个数据进行操作时
# sleep(2)
#
# dr.find_element_by_xpath('//*[@id="searchHotelLevelSelect"]').click()
# #c层级定位   遇到复杂的元素的定位
# wd=dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# for i in wd:
#     i.click()
#     sleep(2)
# dr.quit()
#模拟动作
#send_keys()   输入
#text      获取定位到的元素的文本
#click（）   点击
# clear()    清空定位到的元素上面的数据
# from selenium import  webdriver
# from time import  sleep
# dr=webdriver.Firefox()
# dr=webdriver.Firefox()
# dr.get('https://qzone.qq.com')
# dr.switch_to.frame('login_frame')
# sleep(2)
#回到最开始的页面中
# dr.switch_to.default_ontent()
#回到父框架页面中
# dr.switch_to.parent_frame()
# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys(1258153711)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('special1314...')
# sleep(2)
# dr.find_element_by_id('login_button').click()
# sleep(5)
# dr.quit()

#处理浏览器窗口
# dr.get('https://www.douban.com/')
# #处理浏览器窗口
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[1]/a').click()
# sleep(2)
# dr.switch_to.default_content()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[2]/a').click()
# sleep(2)
# jubing=dr.window_handles
# print(jubing)
#################在京东加入购物车######################
# from selenium  import  webdriver
# from time import sleep
# dr=webdriver.Firefox()
# dr.get('https://www.jd.com/')
# dr.find_element_by_xpath('/html/body/div[1]/div[1]/div/ul[2]/li[1]/a[1]').click()
# sleep(2)
# dr.find_element_by_css_selector('html body div#content div.login-wrap div.w div.login-form div.login-tab.login-tab-r a').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="loginname"]').send_keys(18236549823)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('special1314...')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="loginsubmit"]').click()
# sleep(10)
# dr.find_element_by_xpath('//*[@id="key"]').send_keys('python')
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div[2]/button/i').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[7]/a[3]').click()
# sleep(3)
# jubing=dr.window_handles
# dr.switch_to.window(jubing[-1])
# dr.find_element_by_xpath('//*[@id="GotoShoppingCart"]').click()
# sleep(3)
########################对鼠标的操作############
# from selenium import  webdriver
# from selenium.webdriver.common.action_chains import  ActionChains
# from selenium.webdriver.common.keys import Keys
# import time
# dr=webdriver.Firefox()
# dr.get('https://www.jd.com')
# sleep(2)
# ml=dr.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[1]/div/ul').find_elements_by_tag_name('li')
# print(len(ml))
# dr.quit()
# for i in ml:
#     #控制鼠标移动到元素的位置上    执行
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)
# dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul[2]/li[1]/a[1]').click()
# sleep(2)
# dr.find_element_by_css_selector('html body div#content div.login-wrap div.w div.login-form div.login-tab.login-tab-r a').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="loginname"]').send_keys(18236549823)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('special1314...')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="loginsubmit"]').click()
# sleep(5)
# start=dr.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[3]')
# #drag_and_drop (起始位置，结束位置)
# # drag_and_drop_by_offset(起始位置，x轴坐标，y轴坐标)
# ActionChains(dr).drag_and_drop_by_offset(start,60,0).perform()
#切换到弹出框
# ww=dr.switch_to.alert
# # while True:
# #获取弹出.text)
# #点击确定
# ww.accept()
# sleep(2)
# #点击取消
# ww.dismiss()
# # # #输入
# ww.send_keys('内容')
# sleep(2)
# 框上面的内容
# print(ww
# from selenium import  webdriver
# from selenium.webdriver.common.action_chains import  ActionChains
# from selenium.webdriver.common.keys import Keys
# import time
# import selenium.webdriver.support.ui as ui
# dr=webdriver.Firefox()
# dr.get('https://www.jd.com')
# sleep(2)
#处理页面滚动条  javascript
# for i in range(1,10000,2000):
#     js='var q=document.documentElement.scrollTop=%s'%(i)
#     #执行javascript语句
#     dr.execute_script(js)
#     sleep(2)

#智能等待  设置一个最大等待时间，检测到某个元素出现，就不会继续等待
# unit=ui.WebDriverWait(dr,10)
# #直到定位的元素出现，就不再的等待
# unit.until(lambda dr: dr.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[1]/div/ul/li[1]/a').is_displayed())
# print('hello')
# dr.quit()
#
# from selenium import  webdriver
# from selenium.webdriver.common.action_chains import  ActionChains
# from selenium.webdriver.common.keys import Keys
# import time
# import selenium.webdriver.support.ui as ui
# dr=webdriver.Firefox()
# dr.get('https://www.jd.com')
# sleep(2)
# w=dr.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[4]/a[2]')
# #获取定位到的元素某个属性的值
# a=w.get_attribute('href')
# print(a)
# dr.quit()

#######对qq空间的操作
# import  selenium
# from selenium import  webdriver
# import unittest
# from time import sleep
# import selenium.webdriver.support.ui as ui

# sleep(2)
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys(1258153711)
# sleep(3)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('special1314...')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# dr.quit()



# class Qzone(unittest.TestCase):
#
#     def  set(self):
#         dr = webdriver.Firefox()
#         dr.get('https://qzone.qq.com')
#         dr.switch_to.frame('login_frame')
#         sleep(2)
#         dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
#         sleep(2)
#         dr.find_element_by_xpath('//*[@id="u"]').send_keys(1258153711)
#         sleep(3)
#         dr.find_element_by_xpath('//*[@id="p"]').send_keys('special1314...')
#         sleep(3)
#         dr.find_element_by_xpath('//*[@id="login_button"]').click()
#         sleep(2)
#         return dr.title
#     def test_1(self):
#         self.assertEqual(self.set(),'★、涐de世界、的QQ空间 [http://1258153711.qzone.qq.com]')
# # if __name__=='__main__':
#     unittest.main()
#==================================================
####断言登录qq空间的测试用例
import xlrd
from ddt import data,unpack,ddt
import unittest
from selenium import webdriver
from time import sleep
# def duqu():
#     shuju=[]
#     f = xlrd.open_workbook(r'C:\Users\kong\Desktop\python学习\用户密码.xlsx')
#     sheet = f.sheets()[0]
#     ad=sheet.nrows
#     for i in range(ad):
#         if i ==0:
#             continue
#         else:
#             shuju.append(sheet.row_values(i))
@ddt
class Lonin(unittest.TestCase):



    def  setUp(self):
        self.dr=webdriver.Firefox()
        self.dr.get('https://qzone.qq.com')
    @data([1258153711,'special1314...'])
    @unpack
    def  test_Login(self,u,p):
        self.dr.switch_to.frame('login_frame')
        self.dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="u"]').send_keys(u)
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="p"]').send_keys(p)
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="login_button"]').click()
        sleep(2)
        self.assertEqual(self.dr.title,'★、涐de世界、的QQ空间 [http://1258153711.qzone.qq.com]')
    @data([1258153711,'special1314..'])
    @unpack
    def test_log(self,u,p):
        self.dr.switch_to.frame('login_frame')
        self.dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="u"]').send_keys(u)
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="p"]').send_keys(p)
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="login_button"]').click()
        sleep(2)
        self.assertNotEqual(self.dr.title, '★、涐de世界、的QQ空间 [http://1258153711.qzone.qq.com]')
    def tearDown(self):
        self.dr.quit()
if __name__=='__main__':
    unittest.main()


# import unittest
# from ddt import ddt,data,file_data,unpack
#
# @ddt
# class TestDDT(unittest.TestCase):
#     listb=[]
#     listb.append((1,1))
#     listb.append((2,1))
#     listb.append((3,1))
#     listb.append((4,1))
#     listb.append((5,1))
#     listb.append((6,1))
#     listb.append((7,1))
#     listb.append((8,1))
#     listb.append((9,1))
#     listb.append((11,1))
#     listb.append((12,1))
#     listb.append((13,1))
#     listb.append((14,1))
#     @data(*listb)
#     @unpack
#     def test_addd(self,a,b):
#         c= a+b
#         print(a,b)
#
#
# if __name__ == "__main__":
#     unittest.main()

#######浙江证券业协会##############




