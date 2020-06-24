# -*- encoding=utf8 -*-
__author__ = "ZH"
#导入HTMLTestRunner的包
from package import HTMLTestRunner
#导入test_login的包，执行测试用例时需使用

#from testcase.TC_1login import *
from testcase.TC_2route import *
from utils.log import *
log.info("this is log")

#定义要执行的测试用例的路径
TC_dir = 'C:/Users/FD_Kevin/PycharmProjects/HHCT/testcase'
#定义要执行的测试用例的路径和名称格式
#test_*.py的意思是，./testcase路径下文件名称格式为test_*.py的文件，*为任意匹配，路径下有多少的test_*.py格式的文件，就依次执行几个
discover = unittest.defaultTestLoader.discover(TC_dir, pattern='TC_*.py')

filename = 'C:/Users/FD_Kevin/PycharmProjects/HHCT/testreport/loginReport.html'

#开始执行
if __name__ == '__main__':

    suit=unittest.TestSuite()
    #suit.addTest(Login("login1"))
    #suit.addTest(Logout("logout"))
    suit.addTest(routeE("route5"))

    now = time.strftime("%Y-%m-%d %H_%M_%S")

    #以wb(可写的二进制文件)形式，打开文件，若文件不存在，则先执行创建，再执行打开
    fp = open(filename, 'wb')
    #调用HTMLTestRunner生成报告
    runner = HTMLTestRunner.HTMLTestRunner(
        # 指定测试报告的文件
        stream=fp,
        # 测试报告的标题
        title=u"货车通导航测试报告",
        # 测试报告的副标题
        description=u'用例执行情况（win10 64位）'
    )
    #执行用例,上面定义的suit
    runner.run(suit)

