'''
 @File:log.py
 @DateTime:2021/12/18 17:22
 @Author:lqq
 @use:
 '''

import logging
from config.config import log_path

logger = logging.getLogger() # 定义日志装置
logger.setLevel(logging.INFO) # 设定日志级别
format = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s') # 获取日志内容
logFile = log_path # 定义日志文件路径

fh = logging.FileHandler(logFile,mode='a',encoding='utf-8') # 打开日志文件方式
fh.setLevel(logging.INFO) # 定义文件级别
fh.setFormatter(format) # 日志写入格式
logger.addHandler(fh) # 把文件添加到handler
