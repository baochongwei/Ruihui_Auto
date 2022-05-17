#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-15 13:05

import unittest, pytest
from PLUIAuto_Test_001.function.LoginSystem import *


# 用例
class Test_OF_Login(unittest.TestCase):
    '''
    门户网站的登录验证
    '''
    def setUp(self):
        pass

    def test_1_Login(self):
        """
        验证登录平台首页

        :return:
        """
        # 运行自动化程序，生成测试报告TestResult
        Test_Login = Login_Test_OF_PL().User_Login()

        self.assertEqual(Test_Login,"门户首页", '登录失败')

    def test_2_Login_Fail(self):
        """
        验证断言不符合要求情况下的验证结果

        :return:
        """
        # 运行自动化程序，生成测试报告TestResult
        Test_Login = Login_Test_OF_PL().User_Login()

        self.assertEqual(Test_Login, "门户首页网站", '登录失败')

    def test_3_BAXD_Login(self):
        """
        验证内容待补充

        :return:
        """
        pass

    def tearDown(self):
        pass

# if __name__ == "__main__":
#     unittest.main()