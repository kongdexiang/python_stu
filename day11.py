# !/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,render_template,request
app = Flask(__name__)
print(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login",methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username in ["zhangsan","lisi"] and  password=="123":
            return "<h1>welcome, %s !</h1>" %username
        else:
            return "<h1>login Failure !</h1>"
    else:
        return "<h1>login Failure !</h1>"


if __name__ == '__main__':
    app.run('127.0.0.1',65521)























# dr.find_element_by_xpath('//*[@id="loginUsername"]').send_keys('15638469151')
# sleep(2)
# wd = dr.find_element_by_xpath('/html/body/ul').find_elements_by_tag_name('li')
# for i in wd:
#     if '.com' not in i.text:
#         i.click()





# 通过xpath路径定位
# dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/dl/dd[1]/a').click()
# dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
# 通过css定位
# dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[1]/div[1]/li[2]').click()
# sleep(3)
# dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('18317822978@163.com')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('123456')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userForm"]/div[3]/span/label').click()
# sleep(2)
# wd = dr.find_element_by_xpath('//*[@id="userForm"]/input[7]')
# print(wd.is_enabled())
# wd = dr.find_elements_by_xpath('/html/body/ul/li')
# for i in wd:
#     if i.text == '15638469151':
#         i.click()
#
# sleep(2)
# dr.find_element_by_xpath('//*[@id="loginPassword"]').send_keys('zzzz25210')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login"]').click()
# sleep(3)
# dr.quit()  # 关闭浏览器
#





