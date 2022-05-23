#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-15 13:05

import unittest, pytest
from PLUIAuto_Test_001.function.JLGL_TestSteps import *
from PLUIAuto_Test_001.encapsulation.encapsulation import UIHandle
from PLUIAuto_Test_001.config.config import browser_config


# 用例
class Test_OF_JLGL(unittest.TestCase):
    '''
    计量管理验证计量管理相关功能
    '''
    def setUp(self):
        self.driver = browser_config['chrome']()
        self.uihandle = UIHandle(self.driver)

    def test_1_JLGL_JLWDGL(self):
        """
        计量文档管理创建管理信息

        :return:
        """
        #
        FHXX = JLGL_Test_OF_PL().JLGL_JLTXWDGL_XZML(self.driver,self.uihandle)
        # 通过返回的title判断返回的页面时候符合预期
        self.assertEqual(FHXX,"1", '计量管理模块创建目录失败')


    def tearDown(self):
        self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()