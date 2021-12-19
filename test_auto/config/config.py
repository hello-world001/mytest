'''
 @File:config.py
 @DateTime:2021/12/18 15:54
 @Author:lqq
 @use:
 '''

import sys
import os
# 获取当前路径
# print(os.getcwd())
# print(os.path.dirname(__file__))
# 获取上一层路径
# print(os.path.dirname(os.path.dirname(__file__)))

# driver_path=r"D:\pypytest\script\driver\chromedriver.exe"
driver_path = f"{os.path.dirname(os.path.dirname(__file__))}\driver\chromedriver.exe" # 拼接路径
url= "http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html"
file = r"D:\pypytest\script\data\testdata.xlsx"
sheet = 'login'
log_path = r'D:\pypytest\script\log\log.txt'
