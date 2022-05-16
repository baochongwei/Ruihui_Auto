#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-15 13:20
# constant/constant_1.py
'''
配置系统使用的常量
'''
# Eureka地址，保存在该目录下
EUREKA_URL = 'http://172.18.15.249:10000/'


# 登陆验证地址：审批前端
SPQD_URL = 'http://47.95.39.231:8888/login'

# 登陆验证地址：立案前端
LAQD_URL = "http://172.18.15.249:8082/"

# 登陆验证地址：办案前端
BAQD_URL = "http://172.18.15.249:8080"


# BBH后台管理页面
# 佳霖环境地址
# BBH_Back_Stage = 'http://172.16.1.234:8080/bbh_admin/a/login'
# 测试环境地址
BBH_Back_Stage = 'http://47.95.39.231:7777'

# 获取身份证的网站信息
ID_Number_URL = 'http://sfz.ckd.cc/'

# 公众号登录地址
GZH_URL = 'https://mp.weixin.qq.com/'

# 手机验证码页面
YZM_URL = 'http://221.239.93.143:8080/message/'

"""
各身份前两位地址码
"""
province_id = [11,12,13,14,15,21,22,23,31,32,33,34,35,36,37,41,42,43,44,45,46,
               50,51,52,53,54,61,62,63,65,65,81,82,83]