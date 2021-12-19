'''
 @File:test_login.py
 @DateTime:2021/12/15 21:30
 @Author:lqq
 @use:
 '''

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from pageobjects.pagelogin import Loginpage
from config.config import driver_path,url,file,sheet
from data.read_write import ReadWrite
from log.log import logger
# 测试的是登录模块，所以可以灵活部署
class TestCases(unittest.TestCase):
    def setUp(self):
        '''打开浏览器'''
        s = Service(driver_path)
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.get(url)
        self.page = Loginpage(self.driver)
        self.doc1 = ReadWrite(file,sheet)
    def tearDown(self):
        '''关闭浏览器'''
        self.driver.quit()

    def test_login_success(self):
        '''成功登录'''   # 在测试用例里添加注释可以在测试报告中用例描述栏显示出来
        data_list = self.doc1.read()
        self.page.type_username(data_list[0][0])
        self.page.type_password(data_list[0][1])
        self.page.click_login()

        sleep(2)  # 避免登录中验证失败

        try:
            assert self.driver.title == '我的地盘 - 禅道'  # 断言，验证预期结果和实际结果是否一致
            print('验证登录成功测试----passed')
            logger.info('验证用户登录成功的信息')
            self.page.click_logout()
        except:
            print('验证登录成功测试----failed')

    @unittest.skip('该版本不需要执行')  # 会跳过下面这个测试用例
    def test_wrongpassword(self):
        '''密码错误'''
        data_list = self.doc1.read()
        self.page.type_username(data_list[1][0])
        self.page.type_password(data_list[1][1])
        self.page.click_login()
        sleep(2)
        try:
            alert = self.driver.switch_to.alert
            assert '登录失败' in alert.text
            alert.accept()
            print('验证登录密码错误----pass')
        except:
            print('验证登录密码错误----fail')

    def test_notexistuser(self):
        '''不存在的用户名登录失败'''
        data_list = self.doc1.read()
        self.page.type_username(data_list[2][0])
        self.page.type_password(data_list[2][1])
        self.page.click_login()
        sleep(2)
        try:
            alert = self.driver.switch_to.alert
            assert '登录失败' in alert.text
            alert.accept()
            print('验证不存在的用户名登录失败----pass')
        except:
            print('验证不存在的用户名登录失败----fail')



