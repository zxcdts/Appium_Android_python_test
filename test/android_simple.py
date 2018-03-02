# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/1 下午10:14

import unittest

from action import PageAction


class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        PageAction.open_app()

    def tearDown(self):
        PageAction.quit_app()

    def test_simple_actions(self):
        PageAction.click('accessibility_id', 'Graphics')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
