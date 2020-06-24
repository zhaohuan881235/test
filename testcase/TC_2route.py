# -*- encoding=utf8 -*-
__author__ = "ZH"
import unittest
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from utils.log import *
log.info("this is log")
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# 上滑封装
def swipeup():
    xy = poco.get_screen_size()
    x = xy[0]
    y = xy[1]
    swipe((0.5 * x, 0.7 * y), (0.5 * x, 0.3 * y), duration=1)

class Sroute(unittest.TestCase):
    '滑动地图算路'
    def swiperoute(self):
        # 地图滑动选点算路，普通算路+安全算路
        poco("com.fundrive.truck.mobile:id/rel_browse_map_center").long_click()
        poco("com.fundrive.truck.mobile:id/btn_poi_detail_go_there").click()
        if poco(text="目的地在限行区域内,请确定是否继续设置?").exists():
            poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
            if poco(text="使用安全算路会严格规避限行道路,减少罚款等,也可能无法计算出完全避让的路线,是否算路?").exists():
                poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
                poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
                print("安全算路，终点在限行区域内")
            else:
                poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
                print("普通算路，终点在限行区域内")
        elif poco(text="使用安全算路会严格规避限行道路,减少罚款等,也可能无法计算出完全避让的路线,是否算路?").exists():
            poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
            poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
            print("安全算路，终点在限行区域外")
        else:
            poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
            print("普通算路，终点在限行区域外")


# 检索框输入地址算路，普通算路+安全算路
class routeA(unittest.TestCase):
    ' 检索算路：上海市政府'
    def route1(self):
        poco("com.fundrive.truck.mobile:id/btn_search_title").click()
        text("上海市政府")
        poco("com.fundrive.truck.mobile:id/btn_search").click()
        poco("com.fundrive.truck.mobile:id/btn_go_there").click()

        if poco(text="目的地在限行区域内,请确定是否继续设置?").exists():
            poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
            if poco(text="使用安全算路会严格规避限行道路,减少罚款等,也可能无法计算出完全避让的路线,是否算路?").exists():
                poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
                poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
                poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
                print("安全算路，终点在限行区域内")
            else:
                poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
                poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
                print("普通算路，终点在限行区域内")
        elif poco(text="使用安全算路会严格规避限行道路,减少罚款等,也可能无法计算出完全避让的路线,是否算路?").exists():
            poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
            poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
            poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
            print("安全算路，终点在限行区域外")
        else:
            poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
            poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
            print("普通算路，终点在限行区域外")


# 点击路线按钮地图选点算路，普通算路+安全算路
class routeB(unittest.TestCase):
    def route2(self):
        poco("com.fundrive.truck.mobile:id/btn_route").click()
        poco("com.fundrive.truck.mobile:id/btn_map_choose").click()
        swipeup()
        poco("com.fundrive.truck.mobile:id/btn_poi_ok").click()

        if poco(text="点在限行区域内,请确定是否继续设置?").exists():
            poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
            if poco(text="使用安全算路会严格规避限行道路,减少罚款等,也可能无法计算出完全避让的路线,是否算路?").exists():
                poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
                poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
                poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
                print("安全算路，终点在限行区域内")
            else:
                poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
                poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
                print("普通算路，终点在限行区域内")
        elif poco(text="使用安全算路会严格规避限行道路,减少罚款等,也可能无法计算出完全避让的路线,是否算路?").exists():
            poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
            poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
            poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
            print("安全算路，终点在限行区域外")
        else:
            poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
            poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
            print("普通算路，终点在限行区域外")


# 点击路线按钮输入结果算路，普通算路+安全算路,有BUG暂时无法使用
class routeC(unittest.TestCase):
    '路线按钮检索算路'
    def route3(self):
        poco("com.fundrive.truck.mobile:id/btn_route").click()
        text("上海市政府")
        poco("com.fundrive.truck.mobile:id/btn_ok").click()
        if poco(text="点在限行区域内,请确定是否继续设置?").exists():
            poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
            if poco(text="使用安全算路会严格规避限行道路,减少罚款等,也可能无法计算出完全避让的路线,是否算路?").exists():
                poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
                poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
                poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
                print("安全算路，终点在限行区域内")
            else:
                poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
                poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
                print("普通算路，终点在限行区域内")
        elif poco(text="使用安全算路会严格规避限行道路,减少罚款等,也可能无法计算出完全避让的路线,是否算路?").exists():
            poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
            poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
            poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
            print("安全算路，终点在限行区域外")
        else:
            poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
            poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
            print("普通算路，终点在限行区域外")


# 点击路线按钮收藏夹选点算路，普通算路+安全算路，有BUG暂时无法使用
class routeD(unittest.TestCase):
    '路线收藏算路'
    def route4(self):
        poco("com.fundrive.truck.mobile:id/btn_route").click()
        poco("com.fundrive.truck.mobile:id/btn_top_favorite").click()
        poco(text="上海市政府").click()
        poco("com.fundrive.truck.mobile:id/btn_poi_ok").click()
        if poco(text="点在限行区域内,请确定是否继续设置?").exists():
            poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
            if poco(text="使用安全算路会严格规避限行道路,减少罚款等,也可能无法计算出完全避让的路线,是否算路?").exists():
                poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
                poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
                poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
                print("安全算路，终点在限行区域内")
            else:
                poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
                poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
                print("普通算路，终点在限行区域内")
        elif poco(text="使用安全算路会严格规避限行道路,减少罚款等,也可能无法计算出完全避让的路线,是否算路?").exists():
            poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
            poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
            poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
            print("安全算路，终点在限行区域外")
        else:
            poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
            poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
            print("普通算路，终点在限行区域外")


# 周边搜随机选POI点算路，普通算路+安全算路
class routeE(unittest.TestCase):
    '周边搜POI算路'
    def route5(self):
        poco("com.fundrive.truck.mobile:id/rel_location_nearby").click()
        poco(text="货车停车场").click()
        poco("com.fundrive.truck.mobile:id/btn_go_there").click()
        if poco(text="点在限行区域内,请确定是否继续设置?").exists():
            poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
            if poco(text="使用安全算路会严格规避限行道路,减少罚款等,也可能无法计算出完全避让的路线,是否算路?").exists():
                poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
                poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
                poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
                print("安全算路，终点在限行区域内")
            else:
                poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
                poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
                print("普通算路，终点在限行区域内")
        elif poco(text="使用安全算路会严格规避限行道路,减少罚款等,也可能无法计算出完全避让的路线,是否算路?").exists():
            poco("com.fundrive.truck.mobile:id/dialog_btn2").click()
            poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
            poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
            print("安全算路，终点在限行区域外")
        else:
            poco("com.fundrive.truck.mobile:id/btn_route_method_navi").click()
            poco("com.fundrive.truck.mobile:id/btn_speed_view").exists()
            print("普通算路，终点在限行区域外")


auto_setup(__file__)