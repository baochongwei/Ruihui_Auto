#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-16-02 13:22

# 验证URL是否可运行
from PLUIAuto_Test_001.encapsulation.encapsulation import UIHandle
from PLUIAuto_Test_001.config.config import browser_config
from PLUIAuto_Test_001.function.LoginSystem import *
from PLUIAuto_Test_001.PO.JLGL import locat_config_JLGL
from time import sleep

# import pymysql
# 设置一个全局变量，验证点击进入到登录页面次数

class JLGL_Test_OF_PL():
    """
    验证登录系统
    """
    def __init__(self):
        # 测试报告:  测试合计、 错误情况
        pass

    def JLGL_JLTXWDGL_XZML(self,driver,uihandle):
        """
        计量体系文档管理-新增目录
        :return:返回生成的字典信息
        """
        #　进入系统：
        Login_Test_OF_PL().User_Login(driver, uihandle)
        sleep(3)
        #　点击计量管理
        uihandle.Click(locat_config_JLGL["计量管理根目录"]['计量管理'])
        # 点击计量体系管理
        uihandle.Click(locat_config_JLGL["计量管理根目录"]['计量体系管理'])
        # 点击计量体系文档管理
        uihandle.Click(locat_config_JLGL["计量管理根目录"]['计量体系文档管理'])
        # 返回正确
        return '1'

 # 测试方法，测试完成后，需要注掉
if __name__ == "__main__":
    driver = browser_config['chrome']()
    uihandle = UIHandle(driver)
    b = JLGL_Test_OF_PL().JLGL_JLTXWDGL_XZML(driver,uihandle)
    print(b)


