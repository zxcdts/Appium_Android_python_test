# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/3 下午8:27
from action.PageAction import *

driver = open_app()
click('xpath', "//*[@text='买车']")
click('id',	'com.autohome.usedcar:id/item_car_root')
sleep(5)
swipe(200, 1700, 200, 100)
sleep(5)
driver.current_context
click('xpath', "//android.view.View[contains(@content-desc,'查看全部口碑')]")
click('xpath', "//*[@text='详情']")

click('xpath', "//android.view.View[contains(@content-desc,'收藏')]")
sleep(5)
# driver.current_context
# click('xpath', "//android.view.View[contains(@content-desc,'我要砍价')]")
# sleep(5)
quit_app()
