# -*- encoding=utf8 -*-
__author__ = "ZH"
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.FileHandler('C:/Users/FD_Kevin/PycharmProjects/HHCT/log/log.log')
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)
logger.addHandler(handler)
logger.addHandler(console)

# 在其他模块导入该日志接口module_logger即可
module_logger = logging.getLogger('mainModule.sub')
module_logger.info('this is another module using logging')


# 日志处理类
class log():
    # debug日志
    def debug(msg, *args):
        logger.debug(msg, *args)

    # info日志
    def info(msg, *args):
        logger.info(msg, *args)

    # error日志
    def error(msg, *args):
        logger.error(msg, *args)

    # warn日志
    def warn(msg, *args):
        logger.warn(msg, *args)

    def critical(msg, *args):
        logger.critical(msg, *args)
