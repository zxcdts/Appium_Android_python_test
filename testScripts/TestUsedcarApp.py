# -*- coding: utf-8 -*-
# Author    :zhangbingwei
# Time      :2018/3/2 下午3:07

from action.PageAction import *
from util.ParseExcel import ParseExcel
import traceback
from util.Log import *

# 设置此次测试的环境编码为utf8
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# 创建解析Excel对象
excelObj = ParseExcel()
# 将Excel数据文件加载到内存
excelObj.loadWorkBook(dataFilePath)


# 用例或用例步骤执行结束后，向excel中写执行结果信息
def writeTestResult(sheetObj, rowNo, colsNo, testResult, errorInfo=None, picPath=None):
    # 测试通过结果信息为绿色，失败为红色
    colorDict = {"pass": "green", "faild": "red"}

    # 因为“测试用例”工作表和“用例步骤sheet表”中都有测试执行时间和
    # 测试结果列，定义此字典对象是为了区分具体应该写哪个工作表
    colsDict = {
        "testCase": [testCase_runTime, testCase_testResult],
        "caseStep": [testStep_runTime, testStep_testResult]}
    try:
        # 在测试步骤sheet中，写入测试时间
        excelObj.writeCellCurrentTime(sheetObj,
                                      rowNo=rowNo, colsNo=colsDict[colsNo][0])
        # 在测试步骤sheet中，写入测试结果
        excelObj.writeCell(sheetObj, content=testResult,
                           rowNo=rowNo, colsNo=colsDict[colsNo][1],
                           style=colorDict[testResult])
        if errorInfo and picPath:
            # 在测试步骤sheet中，写入异常信息
            excelObj.writeCell(sheetObj, content=errorInfo,
                               rowNo=rowNo, colsNo=testStep_errorInfo)
            # 在测试步骤sheet中，写入异常截图路径
            excelObj.writeCell(sheetObj, content=picPath,
                               rowNo=rowNo, colsNo=testStep_errorPic)
        else:
            # 在测试步骤sheet中，清空异常信息单元格
            excelObj.writeCell(sheetObj, content="",
                               rowNo=rowNo, colsNo=testStep_errorInfo)
            # 在测试步骤sheet中，清空异常信息单元格
            excelObj.writeCell(sheetObj, content="",
                               rowNo=rowNo, colsNo=testStep_errorPic)
    except Exception, e:
        # 在日志文件中写入详细异常堆栈信息
        logging.debug(u"写excel出错，%s" % traceback.format_exc())


def TestUsedcarApp():
    try:
        # 根据excel文件中的sheet名获取sheet对象
        caseSheet = excelObj.getSheetByName(u"测试用例")
        # 获取测试用例sheet中是否执行列对象
        isExecuteColumn = excelObj.getColumn(caseSheet, testCase_isExecute)
        # 记录执行成功的测试用例个数
        successfulCase = 0
        # 记录需要执行的用例个数
        requiredCase = 0
        for idx, i in enumerate(isExecuteColumn[1:]):
            # 因为用例sheet中第一行为标题行，无需执行
            # print i.value
            # 循环遍历“测试用例”表中的测试用例，执行被设置为执行的用例
            print i
            if i.value.lower() == "y":
                requiredCase += 1
                # 获取“测试用例”表中第idx+2行数据
                caseRow = excelObj.getRow(caseSheet, idx + 2)
                # 获取第idx+2行的“步骤sheet”单元格内容
                caseStepSheetName = caseRow[testCase_testStepSheetName - 1].value
                # print caseStepSheetName

                # 根据用例步骤名获取步骤sheet对象
                stepSheet = excelObj.getSheetByName(caseStepSheetName)
                # 获取步骤sheet中步骤数
                stepNum = excelObj.getRowsNumber(stepSheet)
                # print stepNum
                # 记录测试用例i的步骤成功数
                successfulSteps = 0
                logging.info(u"开始执行用例“%s”" % caseRow[testCase_testCaseName - 1].value)
                for step in xrange(2, stepNum + 1):
                    # 因为步骤sheet中的第一行为标题行，无需执行
                    # 获取步骤sheet中第step行对象
                    stepRow = excelObj.getRow(stepSheet, step)
                    # 获取关键字作为调用的函数名
                    keyWord = stepRow[testStep_keyWords - 1].value
                    # 获取操作元素定位方式作为调用的函数的参数
                    locationType = stepRow[testStep_locationType - 1].value
                    # 获取操作元素的定位表达式作为调用函数的参数
                    locatorExpression = stepRow[testStep_locatorExpression - 1].value
                    # 获取操作值作为调用函数的参数
                    operateValue = stepRow[testStep_operateValue - 1].value

                    # 将操作值为数字类型的数据转成字符串类型，方便字符串拼接
                    if isinstance(operateValue, long):
                        operateValue = str(operateValue)
                    # print keyWord, locationType, locatorExpression, operateValue

                    expressionStr = ""
                    # 构造需要执行的python语句，
                    # 对应的是PageAction.py文件中的页面动作函数调用的字符串表示
                    if keyWord and operateValue and locationType is None and locatorExpression is None:
                        expressionStr = keyWord.strip() + "(u'" + operateValue + "')"
                    elif keyWord and operateValue is None and locationType is None and locatorExpression is None:
                        expressionStr = keyWord.strip() + "()"
                    elif keyWord and locationType and locatorExpression and operateValue:
                        expressionStr = keyWord.strip() + "('" + locationType.strip() + "', '" + locatorExpression.replace(
                            "'", '"').strip() + "', u'" + operateValue + "')"
                    elif keyWord and locationType and locatorExpression and operateValue is None:
                        expressionStr = keyWord.strip() + "('" + locationType.strip() + "', '" + locatorExpression.replace(
                            "'", '"').strip() + "')"
                    # print expressionStr
                    try:
                        # 通过eval函数，将拼接的页面动作函数调用的字符串表示
                        # 当成有效的Python表达式执行，从而执行测试步骤的sheet中
                        # 关键字在ageAction.py文件中对应的映射方法，
                        # 来完成对页面元素的操作
                        eval(expressionStr)
                        # 在测试执行时间列写入执行时间
                        excelObj.writeCellCurrentTime(
                            stepSheet, rowNo=step,
                            colsNo=testStep_runTime)
                    except Exception, e:
                        # 截取异常屏幕图片
                        capturePic = capture_screen()
                        # 获取详细的异常堆栈信息
                        errorInfo = traceback.format_exc()
                        # 在测试步骤Sheet中写入失败信息
                        writeTestResult(
                            stepSheet, step, "caseStep",
                            "faild", errorInfo, capturePic)
                        logging.info(u"步骤“%s”执行失败, 错误信息：%s"
                                     % (stepRow[testStep_testStepDescribe - 1].value,
                                        errorInfo))
                    else:
                        # 在测试步骤Sheet中写入成功信息
                        writeTestResult(stepSheet, step, "caseStep", "pass")
                        # 每成功一步，successfulSteps变量自增1
                        successfulSteps += 1
                        logging.info(u"步骤“%s”执行通过！"
                                     % stepRow[testStep_testStepDescribe - 1].value)
                if successfulSteps == stepNum - 1:
                    # 当测试用例步骤sheet中所有的步骤都执行成功，
                    # 方认为此测试用例执行通过，然后将成功信息写入
                    # 测试用例工作表中，否则写入失败信息
                    writeTestResult(caseSheet, idx + 2, "testCase", "pass")
                    successfulCase += 1
                else:
                    writeTestResult(caseSheet, idx + 2, "testCase", "faild")
        logging.info(u"共%d条用例，%d条需要被执行，本次执行通过%d条。"
                     % (len(isExecuteColumn) - 1, requiredCase, successfulCase))
    except Exception, e:
        # 打印详细的异常堆栈信息
        print traceback.print_exc()

