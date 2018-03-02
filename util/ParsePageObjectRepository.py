# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/1 下午10:14

from ConfigParser import NoSectionError, NoOptionError
import ConfigParser
from ProjectVar.var import Page_Object_Path


class ParsePageObjectRepositoryConfig(object):
    def __init__(self):
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(Page_Object_Path)

    # 获取某个section,所有的key和value,用字典方式返回
    def getItemsFromSection(self, sectionName):
        try:
            results = self.cf.items(sectionName)
        except NoSectionError, e:
            print '没有找到相应的section', sectionName, e.message
        return dict(results)

    # 返回某一个具体的选项对应的value
    def getOptionValue(self, sectionName, optionName):
        try:
            result = self.cf.get(sectionName, optionName)
        except NoSectionError, e:
            print '没有找到相应的section', sectionName, e.message
        except NoOptionError, e:
            print '没有找到相应的option', optionName, e.message
        else:
            return result


if __name__ == '__main__':
    po = ParsePageObjectRepositoryConfig()
    print po.getItemsFromSection('126mail_login')
    print po.getOptionValue('126mail_login', 'login_page.frame')
