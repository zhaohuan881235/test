# -*- encoding=utf8 -*-
__author__ = "ZH"
import unittest
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from utils.log import *
log.info("this is log")
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

class Login(unittest.TestCase):
    '登陆测试'
    def login1(self):
        poco("com.fundrive.truck.mobile:id/btn_user").click()
        if poco(text="登录/注册").exists():
            poco("com.fundrive.truck.mobile:id/iv_portrait").click()
            #清空文本框
            poco("com.fundrive.truck.mobile:id/edt_username").set_text("")
            poco("com.fundrive.truck.mobile:id/edt_username").click()
            text("15380013327")
            poco("com.fundrive.truck.mobile:id/edt_pwd").click()
            text("123456789")
            poco("com.fundrive.truck.mobile:id/btn_login").click()
        #首次登陆有跳过就跳过，没跳过就等待登陆
            if poco(text="跳过").exists():
                poco(text="跳过").click()
            elif poco(text="是否添加本地记录到当前账户").exists():
                poco("com.fundrive.truck.mobile:id/dialog_btn1").click()
                print("登陆成功")
                keyevent("back")
            else:
                wait(Template(r"tpl1588752380592.png", record_pos=(0.023, 0.057), resolution=(1080, 2280)))
                print("登陆成功")

    #如果是登陆状态就退出再登陆
        else:
            poco("com.fundrive.truck.mobile:id/iv_portrait").click()
            poco("com.fundrive.truck.mobile:id/btn_logout").click()
            poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
            poco("com.fundrive.truck.mobile:id/iv_portrait").click()
            #清空文本框
            poco("com.fundrive.truck.mobile:id/edt_username").set_text("")
            poco("com.fundrive.truck.mobile:id/edt_username").click()
            text("15380013327")
            poco("com.fundrive.truck.mobile:id/edt_pwd").click()
            text("123456789")
            poco("com.fundrive.truck.mobile:id/btn_login").click()
        #首次登陆有跳过就跳过，没跳过就等待登陆
            if poco(text="跳过").exists():
                poco(text="跳过").click()
            elif poco(text="是否添加本地记录到当前账户").exists():
                poco("com.fundrive.truck.mobile:id/dialog_btn1").click()
                print("退出后，登陆成功")
                keyevent("back")
            else:
                wait(Template(r"tpl1588752380592.png", record_pos=(0.023, 0.057), resolution=(1080, 2280)))
                print("退出后登陆成功")

class Logout(unittest.TestCase):
    '登出测试'
    def logout(self):
        poco("com.fundrive.truck.mobile:id/btn_user").click()
        if poco(text="登录/注册").exists():
            print("没有登陆，不用退出。")
            keyevent("back")
        else:
            poco("com.fundrive.truck.mobile:id/iv_portrait").click()
            poco("com.fundrive.truck.mobile:id/btn_logout").click()
            poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
            print("退出登陆。")
            keyevent("back")



