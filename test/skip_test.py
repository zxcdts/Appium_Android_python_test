# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/3 下午9:30

from action.PageAction import *

driver = open_app()
skip_ad_wish('id', 'com.autohome.usedcar:id/txt_skip', u'跳过')
sleep(5)
skip_ad_wish('id', 'com.autohome.usedcar:id/txt_skip', u'跳过')
sleep(5)
quit_app()


