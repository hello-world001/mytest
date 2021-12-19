'''
 @File:原testbug.py
 @DateTime:2021/12/18 14:46
 @Author:lqq
 @use:
 '''

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import win32gui
import win32con


class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('打开浏览器')
        s = Service(r"D:\pypytest\script\driver\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)     # Shift+Alt 可以实现批量修改首位
        cls.driver.maximize_window()
        cls.driver.get("http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html")

    @classmethod
    def tearDownClass(cls):
        print('关闭浏览器')
        sleep(5)
        cls.driver.quit()

    def setUp(self):
        print('登录禅道')
        self.driver.find_element(By.ID,'account').send_keys('shelly')
        self.driver.find_element(By.NAME,'password').send_keys('p@ssw0rd')
        self.driver.find_element(By.ID,'submit').click()

    def tearDown(self):
        print('登出禅道')
        self.driver.find_element(By.XPATH,"//a[@class='dropdown-toggle']/span[1]").click()
        self.driver.find_element(By.LINK_TEXT,'退出').click()

    def test_addbug_success(self):
        '''添加bug'''
        sleep(3)
        self.driver.find_element(By.LINK_TEXT,'测试').click()
        self.driver.find_element(By.XPATH,"//nav[@id='subNavbar']/ul/li[1]/a").click()
        self.driver.find_element(By.LINK_TEXT,'提Bug').click()
        self.driver.find_element(By.CLASS_NAME,'search-field').click()
        self.driver.find_element(By.CLASS_NAME,'active-result').click()
        self.driver.find_element(By.ID,'title').send_keys('test')
        sleep(2)
        js = 'var q=document.documentElement.scrollTop=1000'
        self.driver.execute_script(js)
        sleep(1)
        self.driver.find_element(By.XPATH,'//tbody/tr[10]/td[1]/div[1]/div[1]/div[1]/button[1]').click()
        sleep(5)

        dialog = win32gui.FindWindow('#32770','打开')
        ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,'ComboBoxEx32',None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32,0,'ComboBox',None)
        edit = win32gui.FindWindowEx(ComboBox,0,'Edit',None)
        sleep(1)
        button = win32gui.FindWindowEx(dialog,0,'Button','打开(&O)')
        sleep(1)
        win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,r'C:\Users\acer\Pictures\sp.png')
        sleep(5)
        win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)
        sleep(1)
        self.driver.find_element(By.ID,'submit').click()
        sleep(2)
        try:
            self.assertEqual(self.driver.find_element(By.LINK_TEXT,'提Bug').text,'提Bug')
            print('创建Bug成功')
        except:
            print('添加Bug失败')