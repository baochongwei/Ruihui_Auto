#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-15 13:20
# encapsulation/Tools_functions.py

# 封装部分
# 封装常用的非selenium方法
import random
from PLUIAuto_Test_001.constant.constant_1 import province_id
import base64
import os
import datetime
# for test
from PLUIAuto_Test_001.encapsulation.encapsulation import UIHandle
from PLUIAuto_Test_001.config.config import browser_config
from PLUIAuto_Test_001.function.LoginSystem import *

def get_random_str(randomlength=16):
  """
  生成一个指定长度的随机字符串
  :return： 返回生成的字符串
  """
  random_str =''
  base_str ='ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
  length =len(base_str) -1
  for i in range(randomlength):
    random_str +=base_str[random.randint(0, length)]
  return random_str


def get_phone_num():
    """
    生成随机电话号码
    :return:返回生成随机号码
    """
    second_spot = random.choice([3, 4, 5, 7, 8])
    third_spot = {3: random.randint(0, 9),
                  4: random.choice([5, 7, 9]),
                  5: random.choice([i for i in range(10) if i != 4]),
                  7: random.choice([i for i in range(10) if i not in [4, 9]]),
                  8: random.randint(0, 9), }[second_spot]
    remain_spot = random.randint(9999999, 100000000)
    phone_num = "1{}{}{}".format(second_spot, third_spot, remain_spot)
    return phone_num

def get_random_int(startNum = 0, endNumber = 100):
    """
    返回一个随机数值，可以在一定反馈内生成
    也可直接引用random方法调用：如：
    import random
    Number = random.randint(0,50)
    :param startNum:默认为0，最小的数值
    :param endNumber:默认为100，最大的数值区间
    :return:返回数值
    """
    Number = random.randint(startNum,endNumber)
    return Number

# 随机生成身份证号
def get_idnum():
    id_num = ''
    # 随机选择地址码
    id_num+=str(random.choice(province_id))
    # 随机生成4-6位地址码
    for i in range(4):
        ran_num = str(random.randint(0,9))
        id_num+=ran_num
    b = get_birthday()
    id_num+=b
    # 生成15、16位顺序号
    num = ''
    for i in range(2):
        num += str(random.randint(0,9))
    id_num+=num
    # 通过性别判断生成第十七位数字 男单 女双
    s = get_sex()
    if s =='男':
        # 生成奇数
        seventeen_num = random.randrange(1,9,2)
    else:
        seventeen_num = random.randrange(2,9,2)
    id_num+=str(seventeen_num)
    eighteen_num = str(random.randint(1,10))
    if eighteen_num =='10':
        eighteen_num = 'X'
    id_num+=eighteen_num
    return id_num

# 随机生成出生日期
def get_birthday():
    # 随机生成年月日
    year = random.randint(1960,2000)
    month = random.randint(1,12)
    # 判断每个月有多少天随机生成日
    if year%4 ==0:
        if month in (1,3,5,7,8,10,12):
            day = random.randint(1,31)
        elif month in (4,6,9,11):
            day = random.randint(1,30)
        else:
            day = random.randint(1,29)
    else:
        if month in (1,3,5,7,8,10,12):
            day = random.randint(1,31)
        elif month in (4,6,9,11):
            day = random.randint(1,30)
        else:
            day = random.randint(1,28)
    # 小于10的月份前面加0
    if month < 10:
        month = '0' + str(month)
    if day < 10:
        day = '0' + str(day)
    birthday = str(year)+str(month)+str(day)
    return birthday

# 匿名函数
get_sex = lambda :random.choice(['男','女'])

# 截图操作
def GetScreenshot(driver,filename = 1):
    """
    实现截图功能
    :param driver: 生成的driver
    :param filename: 非必填，传入文件名称，例如：aaa,最后会生成aaa.png的图片文件。如果不填，默认按照时间生成，精确到秒
    :return: 无
    """
    # 以天为单位，增加截图文件夹
    now_time_one = datetime.datetime.now()
    # 取当前文件所在路径为绝对路径
    screenshot_dir = os.path.dirname(__file__) + "\log\screenshots_" + datetime.datetime.strftime(now_time_one,"%Y_%m_%d")
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    base64_data = driver.get_screenshot_as_base64()
    png_data = base64.b64decode(base64_data)
    # 判断filename是否传参，如果没有传，默认按照日期生成文件名称；如果传了，按照传的内容生成截图名称
    if(filename == 1):
        now_time = datetime.datetime.now()
        Timesstring = datetime.datetime.strftime(now_time,"%Y_%m_%d_%H_%M_%S.png")
        filename = os.path.join(screenshot_dir,Timesstring)
        with open(filename, 'wb') as f:
            f.write(png_data)
    else:
        filename_New = filename + ".png"
        filename = os.path.join(screenshot_dir, filename_New)
        with open(filename, 'wb') as f:
            f.write(png_data)


# 使用方法和测试方法
# if __name__ == '__main__':
    # print(get_random_str(30))# 返回制定长度随机字符串
    # print(get_phone_num()) # 生成随机电话号码
    # print(get_random_int(0,8000))  # 生成随机数
    # print(get_idnum()) # 生成随机数
    # 截图操作
    # driver = browser_config['chrome']()
    # uihandle = UIHandle(driver)
    # Login_Test_OF_PL().User_Login(driver, uihandle)
    # from PLUIAuto_Test_001.encapsulation.Tools_functions import *  # 引用方法
    # GetScreenshot(driver,"aa") # 生成aa.png
    # GetScreenshot(driver) # 生成操作时间为名称的文件
    # driver.quit()
    # 截图操作结束
