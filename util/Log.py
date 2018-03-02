# encoding=utf-8
import logging.config
from ProjectVar.var import *

# 读取日志的配置文件
logging.config.fileConfig(Logger_conf_path)
# 选择一个日志格式
logger = logging.getLogger("example02")  # example01


def error(message):
    # 打印debug级别的信息
    logger.error(message)


def info(message):
    # 打印 info 级别的信息
    logger.info(message)


def warning(message):
    # 打印 warnging级别的信息
    logger.warning(message)


if __name__ == "__main__":
    info("hi")
    error("world!")
    warning("gloryroad!")
