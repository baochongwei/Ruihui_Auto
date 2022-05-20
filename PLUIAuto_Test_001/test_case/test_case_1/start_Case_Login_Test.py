#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-15 13:05

import unittest, pytest
from PLUIAuto_Test_001.function.LoginSystem import *
from PLUIAuto_Test_001.encapsulation.encapsulation import UIHandle
from PLUIAuto_Test_001.config.config import browser_config


# 用例
class Test_OF_Login(unittest.TestCase):
    '''
    门户网站的登录验证
    '''
    def setUp(self):
        self.driver = browser_config['chrome']()
        self.uihandle = UIHandle(self.driver)

    def test_1_Login(self):
        """
        验证登录平台首页

        :return:
        """
        # 登录系统
        Test_Login = Login_Test_OF_PL().User_Login(self.driver,self.uihandle)
        # 通过返回的title判断返回的页面时候符合预期
        self.assertEqual(Test_Login,"门户首页", '登录失败')

    def test_2_Login_Fail(self):
        """
        验证断言不符合要求情况下的验证结果

        :return:
        """
        # 运行自动化程序，生成测试报告TestResult
        Test_Login = Login_Test_OF_PL().User_Login(self.driver,self.uihandle)
        self.assertEqual(Test_Login, "门户首页网站", '登录失败')

    def test_3_BAXD_Login(self):
        """
        验证内容待补充

        :return:
        """
        pass

    def tearDown(self):
        self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()