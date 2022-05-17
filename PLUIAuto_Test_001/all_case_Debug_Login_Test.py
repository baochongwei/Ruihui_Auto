#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-10 16:34
# all_case.py

import unittest
from PLUIAuto_Test_001 import HTMLTestRunner
import time


# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


# 取test_case文件夹下所有用例文件
def creatsuitel(lists):
    testunit = unittest.TestSuite()
    # discover 方法定义
    discover = unittest.defaultTestLoader.discover(lists, pattern='start_Case_Login_Test.py', top_level_dir=None)
    # 可以修改pattern中的值批量执行脚本
    # 例如：discover = unittest.defaultTestLoader.discover(lists, pattern='start_*.py', top_level_dir=None)
    # 这样回执行所有开头为start_的脚本文件
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

if __name__ == "__main__":
    list_1 = 'test_case\\test_case_1'
    alltestnames = creatsuitel(list_1)
    report_title = u'溥络__页面UI测试'
    desc = u'溥络__页面UI测试脚本V001'

    #取当前时间加入到测试报告文件名中
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename = "report\\"+now+'result.html' #定义个报告存放路径，支持相对路径。
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=report_title, description= desc)
        # 执行测试用例集并生成报告
        runner.run(alltestnames)