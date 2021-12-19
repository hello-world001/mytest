'''
 @File:原testlogin.py
 @DateTime:2021/12/18 14:45
 @Author:lqq
 @use:
 '''

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
# 测试的是登录模块，所以可以灵活部署
class TestCases(unittest.TestCase):
    def setUp(self):
        '''打开浏览器'''
        s = Service(r"D:\pypytest\script\driver\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.get("http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html")

    def tearDown(self):
        '''关闭浏览器'''
        self.driver.quit()

    def test_loginsuccess(self):
        '''成功登录'''   # 在测试用例里添加注释可以在测试报告中用例描述栏显示出来
        self.driver.find_element(By.ID, 'account').send_keys('shelly')
        self.driver.find_element(By.NAME, 'password').send_keys('p@ssw0rd')
        self.driver.find_element(By.ID, 'submit').click()

        sleep(2)  # 避免登录中验证失败

        try:
            assert self.driver.title == '我的地盘 - 禅道'  # 断言，验证预期结果和实际结果是否一致
            print('验证登录成功测试----passed')
            self.driver.find_element(By.XPATH, "//a[@class='dropdown-toggle']/span[1]").click()
            self.driver.find_element(By.LINK_TEXT, '退出').click()
        except:
            print('验证登录成功测试----failed')

    def test_wrongpassword(self):
        '''密码错误'''
        self.driver.find_element(By.ID, 'account').send_keys('shelly')
        self.driver.find_element(By.XPATH, '//tbody/tr[2]/td[1]/input[1]').send_keys('123456')
        self.driver.find_element(By.ID, 'submit').click()
        sleep(2)
        try:
            assert self.driver.title == '我的地盘 - 禅道'  # 断言，验证预期结果和实际结果是否一致
            print('验证登录密码错误----fail')
        except:
            print('验证登录密码错误----pass')
        sleep(2)
        self.driver.find_element(By.ID, 'account').clear()
        self.driver.find_element(By.XPATH, "//input[@name='password']").clear()

    def test_wronguser(self):
        self.driver.find_element(By.ID, 'account').send_keys('abc')
        self.driver.find_element(By.XPATH, '//tbody/tr[2]/td[1]/input[1]').send_keys('123456')
        self.driver.find_element(By.ID, 'submit').click()
        sleep(2)
        try:
            assert self.driver.title == '我的地盘 - 禅道'  # 断言，验证预期结果和实际结果是否一致
            print('验证用户名不存在----fail')
        except:
            print('验证用户名不存在----pass')