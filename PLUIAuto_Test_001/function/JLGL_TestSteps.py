#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-16-02 13:22

# 验证URL是否可运行
from PLUIAuto_Test_001.encapsulation.encapsulation import UIHandle
from PLUIAuto_Test_001.config.config import browser_config
from PLUIAuto_Test_001.function.LoginSystem import *
from PLUIAuto_Test_001.PO.JLGL import locat_config_JLGL
from PLUIAuto_Test_001.encapsulation.Tools_functions import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
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
        # 需要根据iframe 进行跳转，才能够取到右侧页面原始
        driver.switch_to.frame(1)
        # 点击新增目录
        uihandle.Click(locat_config_JLGL["计量体系文档管理页面"]["新增目录"])
        # 弹出页面内容添加
        uihandle.Choose_Element(locat_config_JLGL["计量体系文档管理新增编辑目录"]["所有工厂选项"],1)
        # 生成一个目录名称
        Title_Of_List = get_random_str(10)
        # 目录名称中输入生成的目录名称
        uihandle.Input(locat_config_JLGL["计量体系文档管理新增编辑目录"]["目录名称"],Title_Of_List)
        # 生成、输入备注信息
        String_Of_BZ = get_random_str(99)
        uihandle.Input(locat_config_JLGL["计量体系文档管理新增编辑目录"]["目录备注"],String_Of_BZ)
        # 生成、输入序号信息
        Int_Order = get_random_int(10,50)
        uihandle.Input(locat_config_JLGL["计量体系文档管理新增编辑目录"]["目录序号填写"], Int_Order)
        sleep(1)
        GetScreenshot(driver,"新增目录编辑页面")
        sleep(1)
        # 点击确认按钮
        uihandle.Click(locat_config_JLGL["计量体系文档管理新增编辑目录"]["确定"])
        sleep(3)
        try:
            # 根据名称找到新建的目录，然后执行删除操作
            Xpath_New = ['xpath', "//div[text()='{}']".format(Title_Of_List)]
            uihandle.Click(Xpath_New)
            sleep(1)
            GetScreenshot(driver, "新建目录后的页面")
            sleep(1)
            uihandle.Click(locat_config_JLGL["计量体系文档管理页面"]["删除目录"])
            sleep(1)
            GetScreenshot(driver,"删除新增的目录后的页面")
            sleep(1)
            return "1"
        except TimeoutException:
            return "2"

 # 测试方法，测试完成后，需要注掉
# if __name__ == "__main__":
#     driver = browser_config['chrome']()
#     uihandle = UIHandle(driver)
#     b = JLGL_Test_OF_PL().JLGL_JLTXWDGL_XZML(driver,uihandle)
#     print(b)


