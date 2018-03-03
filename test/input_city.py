# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/3 下午10:43
from action.PageAction import *

driver = open_app()
sleep(5)
click('xpath', "//*[@text='买车']")

click('id',	'com.autohome.usedcar:id/tv_top_left')
click('xpath', "//*[@text='中文/拼音/首字母']")
el = driver.find_element_by_id("com.autohome.usedcar:id/et_search")
print '1111111', el.text
el.send_keys('ali')
print '222222222', el.text
# input_string('id', "com.autohome.usedcar:id/et_search", 'ali')
sleep(100)
quit_app()
