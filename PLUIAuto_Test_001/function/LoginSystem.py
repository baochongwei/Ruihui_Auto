#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-16-02 13:22

# 验证URL是否可运行
from PLUIAuto_Test_001.encapsulation.encapsulation import UIHandle
from PLUIAuto_Test_001.config.config import browser_config
from PLUIAuto_Test_001.config.config import Login_URL, User_Name,Password
from PLUIAuto_Test_001.PO.LoginPage import locat_config_Loginpage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from time import sleep

# import pymysql
# 设置一个全局变量，验证点击进入到登录页面次数

class Login_Test_OF_PL():
    """
    验证登录系统
    """
    def __init__(self):
        # 测试报告:  测试合计、 错误情况
        pass

    def User_Login(self,driver,uihandle):
        """
        登陆系统，获取登陆后的title
        :return:返回生成的字典信息
        """
        uihandle.get(Login_URL)

        # 录入账号
        uihandle.Input(locat_config_Loginpage['登录页面']['用户名'], User_Name)

        # 录入密码
        uihandle.Input(locat_config_Loginpage["登录页面"]['密码'], Password)

        #　点击登录按钮
        uihandle.Click(locat_config_Loginpage["登录页面"]['登陆按钮'])
        # 获取Title
        Title_Login = uihandle.Get_Title()
        # 返回Title值
        return Title_Login

 # 测试方法，测试完成后，需要注掉
if __name__ == "__main__":
    driver = browser_config['chrome']()
    uihandle = UIHandle(driver)
    b = Login_Test_OF_PL().User_Login(driver,uihandle)
    print(b)


