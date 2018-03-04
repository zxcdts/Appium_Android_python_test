# Appium_Android_python_test
## 关键字驱动
    1. 每一个关键字对应的方法(以下称为关键方法)必须能够随时被调用
    2. 关键字必须与关键方法进行关联
    3. 得有一个关键字的解析方式
    4. 执行
## 项目介绍
    1. Appium UI 自动化测试 练手
    2. 环境：Mac 10.12.6；python 2.7.11; Appium 1.7.1
    3. 查看Android apk元素 /Users/xxxx/Library/Android/sdk/tools/bin/uiautomatorviewer 
    4. [u'NATIVE_APP', u'WEBVIEW_com.autohome.usedcar']
    5. ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_addCommands', '_file_detector', '_is_remote', '_mobile', '_switch_to', '_unwrap_value', '_web_element_cls', '_wrap_value', 'activate_ime_engine', 'active_ime_engine', 'add_cookie', 'app_strings', 'application_cache', 'available_ime_engines', 'back', 'background_app', 'capabilities', 'close', 'close_app', 'command_executor', 'context', 'contexts', 'create_web_element', 'current_activity', 'current_context', 'current_url', 'current_window_handle', 'deactivate_ime_engine', 'delete_all_cookies', 'delete_cookie', 'desired_capabilities', 'device_time', 'drag_and_drop', 'end_test_coverage', 'error_handler', 'execute', 'execute_async_script', 'execute_script', 'file_detector', 'file_detector_context', 'find_element', 'find_element_by_accessibility_id', 'find_element_by_android_uiautomator', 'find_element_by_class_name', 'find_element_by_css_selector', 'find_element_by_id', 'find_element_by_ios_predicate', 'find_element_by_ios_uiautomation', 'find_element_by_link_text', 'find_element_by_name', 'find_element_by_partial_link_text', 'find_element_by_tag_name', 'find_element_by_xpath', 'find_elements', 'find_elements_by_accessibility_id', 'find_elements_by_android_uiautomator', 'find_elements_by_class_name', 'find_elements_by_css_selector', 'find_elements_by_id', 'find_elements_by_ios_predicate', 'find_elements_by_ios_uiautomation', 'find_elements_by_link_text', 'find_elements_by_name', 'find_elements_by_partial_link_text', 'find_elements_by_tag_name', 'find_elements_by_xpath', 'flick', 'forward', 'fullscreen_window', 'get', 'get_cookie', 'get_cookies', 'get_log', 'get_screenshot_as_base64', 'get_screenshot_as_file', 'get_screenshot_as_png', 'get_settings', 'get_window_position', 'get_window_rect', 'get_window_size', 'hide_keyboard', 'implicitly_wait', 'install_app', 'is_app_installed', 'is_ime_active', 'keyevent', 'launch_app', 'lock', 'log_types', 'long_press_keycode', 'maximize_window', 'minimize_window', 'mobile', 'name', 'network_connection', 'open_notifications', 'orientation', 'page_source', 'pinch', 'press_keycode', 'pull_file', 'pull_folder', 'push_file', 'quit', 'refresh', 'remove_app', 'reset', 'save_screenshot', 'scroll', 'session_id', 'set_location', 'set_network_connection', 'set_page_load_timeout', 'set_script_timeout', 'set_value', 'set_window_position', 'set_window_rect', 'set_window_size', 'shake', 'start_activity', 'start_client', 'start_session', 'stop_client', 'swipe', 'switch_to', 'switch_to_active_element', 'switch_to_alert', 'switch_to_default_content', 'switch_to_frame', 'switch_to_window', 'tap', 'title', 'toggle_location_services', 'touch_id', 'update_settings', 'w3c', 'wait_activity', 'window_handles', 'zoom']
    6. 滑动 200,1700,200,200 模拟向上滑动
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