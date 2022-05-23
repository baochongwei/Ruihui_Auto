#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-05-17 13:42
# config/config_01.py
# 加一个批注到主干分支
'''
计量管理模块元素信息
'''

# 定位信息维护在此处，维护结构由外到内为：页面名称--页面下元素名称--元素的定位方式+参数
locat_config_JLGL = {
    # 计量管理左侧功能目录结构
    "计量管理根目录":{
        # 计量管理主目录
        "计量管理":['xpath', "//span[text()='计量管理']"],
        # 待办事项目录
        "待办事项":['xpath', "//span[text()='待办事项']"],
        # 系统配置目录
        "系统配置":['xpath', "//span[text()='系统配置']"],
        "工厂维护":['xpath', "//span[text()='工厂维护']"],
        "车间维护":['xpath', "//span[text()='车间维护']"],
        "装置维护":['xpath', "//span[text()='装置维护']"],
        "物料维护":['xpath', "//span[text()='物料维护']"],
        "进出厂点维护":['xpath', "//span[text()='进出厂点维护']"],
        "字典维护":['xpath', "//span[text()='字典维护']"],
        "分工厂字典":['xpath', "//span[text()='分工厂字典']"],
        "流程配置":['xpath', "//span[text()='流程配置']"],
        # 计量体系管理目录
        "计量体系管理":['xpath', "//span[text()='计量体系管理']"],
        "计量体系文档管理":['xpath', "//span[text()='计量体系文档管理']"],
        "计量器具检查通知管理":['xpath', "//span[text()='计量器具检查通知管理']"],
        "计量器具检查管理":['xpath', "//span[text()='计量器具检查管理']"],
        # 计量器具管理
        "计量器具管理":['xpath', "//span[text()='计量器具管理']"],
        "计量器具档案管理":['xpath', "//span[text()='计量器具档案管理']"],
        "计量器具台账管理":['xpath', "//span[text()='计量器具台账管理']"],
        "能源计量网络图管理":['xpath', "//span[text()='能源计量网络图管理']"],
        "计量器具检定计划管理":['xpath', "//span[text()='计量器具检定计划管理']"],
        "计量器具证书管理":['xpath', "//span[text()='计量器具证书管理']"],
        "计量器具检定委托单管理":['xpath', "//span[text()='计量器具检定委托单管理']"],
        "计量器具延期检定管理":['xpath', "//span[text()='计量器具延期检定管理']"],
        # 计量检定管理
        "计量检定管理":['xpath', "//span[text()='计量检定管理']"],
        "检定任务接收":['xpath', "//span[text()='检定任务接收']"],
        "检定过程管理":['xpath', "//span[text()='检定过程管理']"],
        # 计量人员管理
        "计量人员信息管理":['xpath', "//span[text()='计量人员信息管理']"],
        "计量人员管理":['xpath', "//span[text()='计量人员管理']"],
        "计量人员证书信息管理":['xpath', "//span[text()='计量人员证书信息管理']"],
        "计量人员培训管理":['xpath', "//span[text()='计量人员培训管理']"],
        # 计量数据管理
        "计量数据管理":['xpath', "//span[text()='计量数据管理']"],
        "进场数据管理":['xpath', "//span[text()='进场数据管理']"],
        "出厂数据管理":['xpath', "//span[text()='出厂数据管理']"],
        "计量仪表状态检测管理":['xpath', "//span[text()='计量仪表状态检测管理']"],
        "进厂数据比对分析":['xpath', "//span[text()='进厂数据比对分析']"],
        "出厂数据比对分析":['xpath', "//span[text()='出厂数据比对分析']"],
        "管输比对模型配置":['xpath', "//span[text()='管输比对模型配置']"],
        "皮带秤比对模型配置":['xpath', "//span[text()='皮带秤比对模型配置']"],
        "计量报表管理":['xpath', "//span[text()='计量报表管理']"],
        # 计量纠纷管理
        "计量纠纷管理":['xpath', "//span[text()='计量纠纷管理']"],
        "内部计量纠纷管理":['xpath', "//span[text()='内部计量纠纷管理']"],
        "外部计量纠纷管理":['xpath', "//span[text()='外部计量纠纷管理']"],
        # 计量器具综合展示
        "计量器具综合展示":['xpath', "//span[text()='计量器具综合展示']"],
        "进厂数据展示":['xpath', "//span[text()='进厂数据展示']"],
        "出厂数据展示":['xpath', "//span[text()='出厂数据展示']"],
        "器具综合展示":['xpath', "//span[text()='器具综合展示']"],
    },
    # 计量体系文档管理右侧功能元素
    "计量体系文档管理页面":{
        # 主页面按钮
        "新增目录":['xpath', "//span[text()='新增目录']"],
        "编辑目录":['xpath', "//span[text()='编辑目录']"],
        "删除目录":['xpath', "//span[text()='删除目录']"],
        "新增文件":['xpath', "//span[text()='新增文件']"],
        "编辑文件":['xpath', "//span[text()='编辑文件']"],
        "删除文件":['xpath', "//span[text()='删除文件']"],
    },
    # 新增/编辑目录页面
    "计量体系文档管理新增编辑目录":{
        "所有工厂选项":["xpath", "/html/body/div[1]/section/section/main/div/div[4]/div/div/div[2]/form/div[1]/div/div/div/input"],
        "所有工厂首选":["xpath", "//span[text()='生产工厂']"],
        "目录名称":["xpath", "/html/body/div[1]/section/section/main/div/div[4]/div/div/div[2]/form/div[2]/div/div/input"],
        "目录备注":["xpath", "/html/body/div[1]/section/section/main/div/div[4]/div/div/div[2]/form/div[3]/div/div/textarea"],
        "目录序号填写":["xpath", "/html/body/div[1]/section/section/main/div/div[4]/div/div/div[2]/form/div[4]/div/div/div/input"],
        "目录序号上移":["xpath", "/html/body/div[1]/section/section/main/div/div[4]/div/div/div[2]/form/div[4]/div/div/span[2]"],
        "目录序号下移":["xpath", "/html/body/div[1]/section/section/main/div/div[4]/div/div/div[2]/form/div[4]/div/div/span[1]"],
        "确定":["xpath", "/html/body/div[1]/section/section/main/div/div[4]/div/div/div[3]/span/button[2]"],
        "取消":["xpath", "/html/body/div[1]/section/section/main/div/div[4]/div/div/div[3]/span/button[1]"],

    }
}

#  //a[text()=‘百度搜索’]
#
# 或者 //a[contains(text(),“百度搜索”)]
