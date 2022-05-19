#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-11 13:42
# config/config_01.py
'''
config文件，配置写这
'''

# 定位信息维护在此处，维护结构由外到内为：页面名称--页面下元素名称--元素的定位方式+参数
locat_config_Loginpage = {
    "登录页面":{
        "用户名":['xpath', '//*[@id="username"]'],
        "密码":["xpath", "//*[@id='password']"],
        "登陆按钮": ["xpath", "//*[@name='submit']"],
    }
}

#  //a[text()=‘百度搜索’]
#
# 或者 //a[contains(text(),“百度搜索”)]