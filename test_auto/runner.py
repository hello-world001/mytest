'''
 @File:runner.py
 @DateTime:2021/12/15 21:40
 @Author:lqq
 @use:
 '''

import unittest
from BeautifulReport import BeautifulReport  # 生成测试报告

# 加载测试用例
cases=unittest.defaultTestLoader.discover(start_dir=r'D:\pypytest\script\cases',pattern='test*.py') #start_dir是测试用例存储路径，pattern是选择要运行以test开头的文件
# 执行测试用例
result=BeautifulReport(cases)
# 生成测试报告
result.report(description='禅道测试报告',filename='lqq测试报告',report_dir=r'D:\pypytest\script\report') #description是生成测试报告标题，filename是存储文件名，report_dir是报告存储路径