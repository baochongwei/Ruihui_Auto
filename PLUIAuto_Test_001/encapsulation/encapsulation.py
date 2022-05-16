#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-15 13:20
# encapsulation/encapsulation.py

# 封装部分
# 主要封装来源于Selenium webdriver中的基础方法，统一使用了隐式等待方式
from PLUIAuto_Test_001.PO.LoginPage import locat_config
from PLUIAuto_Test_001.log.log import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class UIHandle():
    driver = None
    logger = Logger()

    # 构造方法，用来接收selenium的driver对象
    @classmethod
    def __init__(cls, driver):
        cls.driver = driver

    # 输入地址
    @classmethod
    def get(cls, url):
        cls.logger.loginfo(url)
        cls.driver.get(url)
        cls.Window_Maxsize()

    # 关闭浏览器驱动
    @classmethod
    def quit(cls):
        cls.driver.quit()

    # element对象（还可加入try，截图等。。。）
    @classmethod
    def element(cls, page, element):
        # 加入日志
        cls.logger.loginfo(page)
        # 加入隐性等待
        # 此处便可以传入config_o1中的dict定位参数
        el = WebDriverWait(cls.driver, 10).until(EC.presence_of_element_located(locat_config[page][element]))
        cls.hightlight(el)
        # 加入日志
        cls.logger.loginfo(page + '_' + element +' OK')
        return el
    # element对象(还未完成。。。)\
    @classmethod
    def elements(cls, page, element):
        # 加入日志
        cls.logger.loginfo(page)
        # 加入隐性等待
        WebDriverWait(cls.driver, 10)
        els = cls.driver.find_elements_by_class_name(locat_config[page][element])
        # 加入日志
        cls.logger.loginfo(page + '_' + element +' OK')
        # 注意返回的是list
        return els

    @classmethod  # 使用tag 寻找字段
    def elements_tag(cls, page, element):
        # 加入日志
        cls.logger.loginfo(page)
        # 加入隐性等待
        WebDriverWait(cls.driver, 10)
        els = cls.driver.find_elements_by_tag_name(locat_config[page][element])
        # print u'验证字段是否取到'

        # 加入日志
        cls.logger.loginfo(page + '_' + element +' OK')
        # 注意返回的是list
        return els

    @classmethod  # 使用class 寻找字段
    def elements_class(cls, page, element):
        # 加入日志
        cls.logger.loginfo(page)
        # 加入隐性等待
        WebDriverWait(cls.driver, 10)
        els = cls.driver.find_elements_by_class_name(locat_config[page][element])

        # 加入日志
        cls.logger.loginfo(page + '_' + element +' OK')
        # 注意返回的是list
        return els

    @classmethod  # 使用class 寻找字段
    def elements_id(cls, page, element):
        # 加入日志
        cls.logger.loginfo(page)
        # 加入隐性等待
        WebDriverWait(cls.driver, 10)
        els = cls.driver.find_elements_by_id_name(locat_config[page][element])

        # 加入日志
        cls.logger.loginfo(page + '_' + element +' OK')
        # 注意返回的是list
        return els

    # send_keys方法
    @classmethod
    def Input(cls, page, element, msg):
        el = cls.element(page, element)
        el.clear()
        el.send_keys(msg)
        sleep(1)

    # click方法
    @classmethod
    def Click(cls, page, element):
        el = cls.element(page, element)
        el.click()
        sleep(1)

    # 日期控件
    @classmethod
    def Date_Option(cls, page,element,ID ,Date):
        """
        design by : Bierante
        :param page: 页面
        :param element: 元素名称
        :param ID: 页面中元素对应ID
        :param Date: 录入当前日期
        :return:
        function: 向日期控件录入想要录入的时间
        """
        el = cls.element(page, element)
        js = "document.getElementById('%s').removeAttribute('readonly')" % ID
        cls.driver.execute_script(js)
        el.send_keys(str(Date.date()))

    # 获取元素描述
    @classmethod
    def Get_Text(cls, page,element):
        """
        design by : Bierante
        :param page: 页面
        :param element: 元素对应中文
        :return:
        function : 获取元素对应的页面内容
        """
        el = cls.element(page , element)
        return el.text
    # 获取列数据
    @classmethod
    def Get_Texts(cls, page, element):
        """

        :param page: 页面
        :param element: 元素对应中文
        :return:
        """
        el = cls.elements(page, element)
        text = []
        for eli in el:
            text.append(eli.text)
        return text

    # 获取列数据,通过tag名称获取，会同时获取tag名称相同的所有数据，并返回一个列表
    @classmethod
    def Get_Texts_tag(cls, page, element):
        """
        :param page: 页面
        :param element: 元素对应中文
        :return:
        """
        el = cls.elements_tag(page, element)
        text = []
        for eli in el:
            # print eli.text
            text.append(eli.text)
        return text

        # 获取列数据,通过tag名称获取，会同时获取tag名称相同的所有数据，并返回一个列表
    @classmethod
    def Get_Texts_id(cls, page, element):
        """
        :param page: 页面
        :param element: 元素对应中文
        :return:
        """
        el = cls.elements_id(page, element)
        text = []
        for eli in el:
            # print eli.text
            text.append(eli.text)
        return text

    @classmethod  # 通过class_name 批量查找字段
    def Get_Texts_class(cls, page, element):
        """

        :param page: 页面
        :param element: 元素对应中文
        :return:
        """
        el = cls.elements_class(page, element)
        text = []
        for eli in el:
            text.append(eli.text)
        return text
    # 点击获取元素
    @classmethod
    def Clicks(cls, page, element):
        """

        :param page: 页面
        :param element: 元素对应中文
        :return:
        """
        el = cls.elements(page, element)
        for eli in el:
            eli.click()
            sleep(1)
    # 点击获取元素
    @classmethod
    def Clicks_Tag(cls, Num,page, element):
        """

        :param page: 页面
        :param element: 元素对应中文
        :return:
        """
        el = cls.elements_tag(page, element)
        Click_Num = Num -1
        el[Click_Num].click()

    # 点击获取元素
    @classmethod
    def Clicks_Class(cls, Num,page, element):
        """

        :param page: 页面
        :param element: 元素对应中文
        :return:
        """
        el = cls.elements_class(page, element)
        Click_Num = Num -1
        el[Click_Num].click()
    # 特殊点击--选项圆点
    @classmethod
    def Circle_Click(cls, page, element):
        el = cls.element(page, element)
        el.find_element_by_tag_name('Input')
        print (u'选项点击完毕')
        el.click()

    # 清除数据项内容
    @classmethod
    def Clear(cls, page, element,ID):
        """
        清空功能，针对只读控件
        :param page:  页面名称
        :param element:  元素名称
        :param ID:  元素id
        :return:
        """
        el = cls.element(page, element)
        js = "document.getElementById('%s').removeAttribute('readonly')" % ID
        cls.driver.execute_script(js)
        el.clear()

    @classmethod
    def Clear_Ordinary(cls, page, element):
        """
        普通的清空功能
        :param page:  页面名称
        :param element:  元素名称
        :param ID:  元素id
        :return:
        """
        el = cls.element(page, element)
        el.clear()
    # 获取元素描述
    @classmethod
    def Get_Attribute(cls, page,element):
        """
        design by : Bierante
        :param page: 页面
        :param element: 元素对应中文
        :return:
        function : 获取元素对应的页面内容
        """
        el = cls.element(page , element)
        return el.get_attribute('ng-reflect-model')

    # 最大化页面
    @classmethod
    def Window_Maxsize(cls):
        """

        :return:
        """
        cls.driver.maximize_window()

    # 修改操作内容背景色
    @classmethod
    def hightlight(cls, element):
        """
        元素高亮显示
        :param element: 元素对象
        :return: 无
        """
        cls.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                   element, "border: 2px solid red;")

    #　获取进入页面的title
    @classmethod
    def Get_Title(cls):
        """
        捕捉title并返回
        :return:
        """
        Str_Title = cls.driver.title
        return Str_Title