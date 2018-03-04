# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/3 下午8:27
from action.PageAction import *
from util.ObjectMap import *
from appium.webdriver.common.touch_action import TouchAction

driver = open_app()
click('xpath', "//*[@text='买车']")
click('id',	'com.autohome.usedcar:id/item_car_root')
sleep(5)
swipe(200, 1700, 200, 100)
sleep(5)
driver.current_context
sleep(5)
click('xpath', "//android.view.View[contains(@content-desc,'查看全部口碑')]")
# els0 = getElementBy(driver, 'xpath', "//android.view.View[contains(@content-desc,'查看全部口碑')]")
# print els0
# els0.click()
# sleep(3)
el1 = getElementBy(driver, 'xpath', "//android.view.View[contains(@content-desc,'收藏')]")
print el1.location.get('x'), el1.location.get('y')
print dir(el1)
TouchAction(driver).tap(x=el1.location.get('x'), y=el1.location.get('y')).perform()
# execute_jsscript('collect')
# driver.execute_script("window.document.getElementById('collect').click()")
sleep(10)
# driver.current_context
# click('xpath', "//android.view.View[contains(@content-desc,'我要砍价')]")
# sleep(5)
quit_app()
