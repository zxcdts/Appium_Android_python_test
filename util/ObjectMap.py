# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/2 下午2:20

from selenium.webdriver.support.ui import WebDriverWait


def getElementBy(driver, locationType, locatorExpression):
    try:
        if locationType == 'id':
            element = WebDriverWait(driver, 15).until(lambda x: x.find_element_by_id(locatorExpression))
        elif locationType == 'accessibility_id':
            element = WebDriverWait(driver, 15).until(lambda x: x.find_element_by_accessibility_id(locatorExpression))
        elif locationType == 'xpath':
            element = WebDriverWait(driver, 15).until(lambda x: x.find_element_by_xpath(locatorExpression))
        elif locationType == 'link_text':
            element = WebDriverWait(driver, 15).until(lambda x: x.find_element_by_partial_link_text(locatorExpression))
        return element
    except Exception, e:
        raise e


def getElementByWithoutWait(driver, locationType, locatorExpression):
    try:
        if locationType == 'id':
            element = driver.find_element_by_id(locatorExpression)
        elif locationType == 'accessibility_id':
            element = driver.find_element_by_accessibility_id(locatorExpression)
        elif locationType == 'xpath':
            element = driver.find_element_by_xpath(locatorExpression)
        elif locationType == 'link_text':
            element = driver.find_element_by_partial_link_text(locatorExpression)
        return element
    except Exception, e:
        raise e