#!/usr/bin/python
#-*- coding:utf-8 -*-

# import  unittest
# from selenium import webdriver
# from time import sleep
#
#
# class zhengjiang(unittest.TestCase):
#
#     def  setUp(self):
#         self.dr=webdriver.Firefox()
#         self.dr.get('https://ai.taobao.com/')
#     def test_01(self):
#         self.dr.find_element_by_xpath('/html/body/div[1]/div/ul[1]/li[2]/div/a[1]').click()
#         sleep(2)
#         self.dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div[4]/div/div[5]/a[1]').click()
#         sleep(2)
#         self.dr.find_element_by_id('TPL_username_1').send_keys('qq1258153711')
#         sleep(2)
#         self.dr.find_element_by_id('TPL_password_1').send_keys('special1314...')
#         sleep(2)
#         self.dr.find_element_by_id('J_SubmitStatic').click()
#         sleep(3)
#         self.assertEqual(self.dr.title,'爱淘宝-淘宝网购物分享平台')
#
#     def tearDown(self):
#
#         self.dr.quit()
# if __name__=='__main__':
#     unittest.main()
#
# import  unittest
# from selenium import webdriver
# from time import sleep
# import selenium.webdriver.support.ui as ui
# class  moer_jingying(unittest.TestCase):
#
#     def setUp(self):
#         self.dr = webdriver.Firefox()
#         sleep(3)
#         self.dr.get('http://www.moore.ren')
#         sleep(10)
#
#     def  test_01zhuce(self):
#         self.dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/li[1]/a').click()
#         sleep(2)
#         lit=self.dr.window_handles
#         self.dr.switch_to.window(lit[-1])
#         sleep(2)
#         self.dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys(18236549823)
#         sleep(2)
#         self.dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('special1314')
#         sleep(3)
#         self.dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/form/div[3]/span/label').click()
#         sleep(1)
#         self.dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/form/input[1]').click()
#         sleep(5)
#         w=self.dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/li/a')
#         self.assertEqual(self.dr.title,'摩尔人招聘-专业的半导体招聘平台-半导体人才网-半导体工作')
#     def tearDown(self):
#         self.dr.quit()
# if __name__=='__main__':
#     unittest.main()

import xlrd
class  Excel_data():

    def __init__(self,Excelname,sheetname='Sheet1'):
        self.data=xlrd.open_workbook(Excelname)
        self.sheet=self.data.sheet_by_name(sheetname)
        self.keys=self.sheet.row_values(0)
        self.rowN=self.sheet.nrows
        self.colN=self.sheet.ncols
    def duqu_zidian(self):
        if self.rowN <=1:
            print('这是keys')
        else:
            d=[]

            for  i in range(1,self.rowN):

               val = self.sheet.row_values(i)
               for k in range(self.colN):
                   s={}

                   s[self.keys[k]]=val[k]
                   d.append(s)
            return d
if __name__ =='__main__':
    celname='用户密码.xlsx'
    data=Excel_data(celname)
    print(data.duqu_zidian())




