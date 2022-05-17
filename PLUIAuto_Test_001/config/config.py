#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-11 13:42
# config/config_01.py
'''
config文件，配置写这
'''
from selenium import webdriver

# config配置部分

# 浏览器种类维护在此处
browser_config = {
    'ie': webdriver.Ie,
    'chrome': webdriver.Chrome
}

# 稳定环境地址
Login_URL = "http://sso.iplenmes.cn:8031/cas/login?service=http%3A%2F%2Fwww.iplenmes.cn%2Fportal%2F" # 配置所有取得的URL地址
User_Name = "admin" # 登录的账号信息
Password = "Admin@123" # 登录的测试密码
