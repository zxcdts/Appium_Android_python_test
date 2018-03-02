# encoding=utf-8

from appium import webdriver
from util import Log
from util.ObjectMap import *
from util.DirAndTime import *

# 定义全局driver变量
driver = None


# 打开app
def open_app():
    global driver
    try:
        desired_caps = {}
        desired_caps['platformName'] = platformName
        desired_caps['platformVersion'] = platformVersion
        desired_caps['deviceName'] = deviceName
        desired_caps['app'] = app_Path
        desired_caps['noReset'] = noReset

        driver = webdriver.Remote(driver_remote, desired_caps)
    except Exception, e:
        raise e


# 重置应用
def reset_app():
    global driver
    try:
        if driver is not None:
            driver.reset()
        else:
            Log.error('driver is None')
    except Exception, e:
        raise e


# 退出脚本运行并关闭每个相关的窗口连接
def quit_app():
    global driver
    try:
        if driver is not None:
            driver.quit()
        else:
            Log.error('driver is None')
    except Exception, e:
        raise e


# 查找元素，并点击，需要参数为定位类型与定位表达式
def click(locationType, locatorExpression, *arg):
    # 点击页面元素
    global driver
    try:
        getElementBy(driver, locationType, locatorExpression).click()
    except Exception, e:
        raise e


# 页面滑动
# 如果起始的X与结束的X相同，则表示上下滑动
# 如果起始的Y与结束的Y相同，则表示左右滑动
# 如果操作存在懒加载的页面，则需要加上duration，否则底部元素无法显示
def swipe(start_x, start_y, end_x, end_y, duration=None):
    global driver
    try:
        driver.swipe(start_x, start_y, end_x, end_y, duration)
    except Exception, e:
        raise e


# 截屏并保存图片
def capture_screen(*args):
    # 截取屏幕图片
    global driver
    currTime = getCurrentTime()
    picNameAndPath = str(createCurrentDateDir()) + "/" + str(currTime) + ".png"
    try:
        driver.get_screenshot_as_file(picNameAndPath.replace('/', r'/'))
    except Exception, e:
        raise e
    else:
        return picNameAndPath


# 如果存在则跳过的广告
def skip_ad_wish(locationType, locatorExpression, assertString):
    # 点击页面元素
    global driver
    try:
        if assertString in driver.page_source:
            el = getElementBy(driver, locationType, locatorExpression)
            el.click()
        else:
            pass
    except Exception, e:
        raise e


# 如果存在，则全部允许
def allow_permission(locatorExpression='com.android.packageinstaller:id/permission_allow_button'):
    global driver
    try:
        el = getElementBy(driver, 'id', locatorExpression)
        if el is not None:
            el.click()
    except Exception, e:
        raise e


# 断言页面源码是否存在某关键字或关键字符串
def assert_string_in_pagesource(assertString, *arg):
    global driver
    try:
        assert assertString in driver.page_source, u"%s not found in page source!" % assertString
    except AssertionError, e:
        raise AssertionError(e)
    except Exception, e:
        raise e


# 断言页面源码是否不存在某关键字或关键字符串
def assert_string_notin_pagesource(assertString, *arg):
    global driver
    try:
        if assertString not in driver.page_source:
            assert True, u"%s not found in page source!" % assertString
        else:
            assert False, u"%s found in page source!" % assertString
    except AssertionError, e:
        raise AssertionError(e)
    except Exception, e:
        raise e


# 在页面输入框中输入数据
def input_string(locationType, locatorExpression, inputContent):
    global driver
    try:
        el = getElementBy(driver, locationType, locatorExpression)
        el.clear()
        el.send_keys(inputContent)
    except Exception, e:
        raise e


# 强制等待
def sleep(sleepSeconds, *arg):
    try:
        time.sleep(int(sleepSeconds))
    except Exception, e:
        raise e


# 跳转到特定activity
def start_activity(app_package, app_activity, *arg):
    global driver
    try:
        driver.start_activity(app_package, app_activity)
    except Exception, e:
        raise e
