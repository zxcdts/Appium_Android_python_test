# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/1 下午10:14
import os

project_path = os.path.dirname(os.path.dirname(__file__))
Page_Object_Path = project_path + '/Conf/PageObjectRepository.ini'
Logger_conf_path = project_path + '/Conf/Logger.conf'

# 异常截图存放目录绝对路径
screenPicturesDir = project_path + "/exceptionpictures/"

# 异常截图存放目录绝对路径
correctpictures = project_path + "/correctpictures/"

# 测试数据文件存放绝对路径
dataFilePath = project_path + u"/testData/二手车测试用例.xlsx"

# desired_caps
app_Path = project_path + '/app/usedcar_be_ta.apk'
platformName = 'Android'
platformVersion = '6.0'
deviceName = 'MZJZFQS8WOFEP7'
noReset = 'True'

driver_remote = 'http://localhost:4723/wd/hub'

# 用例Excel相应参数
# 测试数据文件中，测试用例表中部分列对应的数字序号
testCase_testCaseName = 2
testCase_testStepSheetName = 4
testCase_isExecute = 5
testCase_runTime = 6
testCase_testResult = 7

# 用例步骤表中，部分列对应的数字序号
testStep_testStepDescribe = 2
testStep_keyWords = 3
testStep_locationType = 4
testStep_locatorExpression = 5
testStep_operateValue = 6
testStep_runTime = 7
testStep_testResult = 8
testStep_errorInfo = 9
testStep_errorPic = 10
