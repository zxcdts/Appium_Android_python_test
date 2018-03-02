# Appium_Android_python_test
## 项目介绍
    1. Appium UI 自动化测试 练手
    2. 环境：Mac 10.12.6；python 2.7.11; Appium 1.7.1
    3. 查看Android apk元素 /Users/xxxx/Library/Android/sdk/tools/bin/uiautomatorviewer 
## 项目结构
    1. action    关键字方法，包含查找、滑动、断言
    2. app    存放安装包
    3. Conf    日志的配置文件，以及后期增加其他配置信息
    4. exceptionpictures    存放失败后的截图
    5. ProjectVar    整个系统中用到的参数，比如启动appium
    6. testData    测试用例Excel
    7. testScripts    读取测试用例中关键字并执行
    8. util    基础方法，比如获取路径、时间、解析Excel、解析配置文件、解析ini文件
    9. test    测试使用
    RunTest.py    整个项目的执行入口