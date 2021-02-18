from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC  # expected_conditions 预期条件
from base.read_config_file import read_ini
from pykeyboard import PyKeyboard  # 模拟键盘输入
from selenium.webdriver.common.action_chains import ActionChains  # 主要实现鼠标移动，鼠标按键动作，按键和上下文菜单交互。
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from base.handle_json import handle_json
from base.ShowapiRequest import ShowapiRequest
from PIL import Image
import os
import time
import random


class SeleniumDriver:
    # def __init__(self, browser):
    #     self.driver = self.open_browser(browser)

    def open_browser(self, browser):
        if browser.upper() == 'CHROME':
            options = webdriver.ChromeOptions()
            prefs = {'download.default_directory': '\\Users\\xiachengpeng\\Downloads',
                     'profile.default_content_settings.popups': 0}
            # download.default_directory 设置下载路径  profile.default_content_settings.popups  禁止弹窗
            options.add_experimental_option("prefs", prefs)
            self.driver = webdriver.Chrome(options=options)
        elif browser.upper() == 'FIREFOX':
            profile = webdriver.FirefoxProfile()
            profile.set_preference('browser.download.dir', '\\Users\\xiachengpeng\\Downloads')
            profile.set_preference('browser.download.folderList', 2)
            profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
            self.driver = webdriver.Firefox(firefox_profile=profile)
        else:
            self.driver = webdriver.Safari()
        time.sleep(2)
        return self.driver

    def get_url(self, url):
        if self.driver is not None:
            if "http://" in url:
                self.driver.get(url)
            else:
                print("url有问题")
        else:
            print("case失败")

    def get_cookie(self):
        """
        写入cookie
        """
        cookie = self.driver.get_cookies()
        handle_json.write_data(cookie)

    def set_cookie(self):
        """
        植入cookie
        """
        self.driver.delete_all_cookies()
        cookie = handle_json.get_data()
        time.sleep(2)
        self.driver.add_cookie(cookie)

    def handle_window(self, *ages):
        value = len(ages)
        if value == 1:
            if ages[0] == "max":
                self.driver.maximize_window()
            elif ages[0] == "min":
                self.driver.minimize_window()
            elif ages[0] == "back":
                self.driver.back()
            elif ages[0] == "forward":
                self.driver.forward()
            elif ages[0] == "refresh":
                self.driver.refresh()
            else:
                return None
        elif value == 2:
            self.driver.set_window_size(ages[0], ages[1])
        else:
            return None
        time.sleep(2)

    def get_title(self):
        """
        获取title
        """
        title = self.driver.title
        return title

    def assert_title(self, title_name=None):
        """
        断言 title是否正确
        """
        if title_name is not None:
            get_title = EC.title_contains(title_name)  # 判断标题是否包含传入的参数
            return get_title(self.driver)

    def open_url_ture(self, url, title_name=None):
        """
        通过title判断页面是否正确
        """
        self.get_url(url)
        return self.assert_title(title_name)

    def switch_windows(self, title_name=None):
        """
        切换windows
        """
        handle_list = self.driver.window_handles  # 返回当前所有窗口的句柄
        current_handle = self.driver.current_window_handle  # 返回当前窗口的句柄
        for i in handle_list:
            if i != current_handle:
                time.sleep(1)
                self.driver.switch_to.window(i)
                if self.assert_title(title_name):
                    break
                ti = EC.title_contains("网站连接")
                if ti(self.driver):
                    break

    def refresh_f5(self):
        """
        强制刷新
        """
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL)

    def switch_iframe(self, send_key, info=None):
        """
        切换iframe,传入element就切入，不传就切出
        """
        if info is None:
            self.driver.switch_to.default_content()
        else:
            iframe_element = self.get_element(info)
            element = self.driver.switch_to.frame(iframe_element)
            ActionChains(self.driver).move_to_element(element).click().send_keys(send_key).perform()

    def switch_alert(self, value, key=None):
        """
        系统级弹窗
        """
        windows_alert = self.driver.switch_to.alert
        if value == "accept":
            if key is None:
                windows_alert.accept()
            else:
                windows_alert.send_keys(key)
                windows_alert.accept()
        else:
            windows_alert.dismiss()

    def element_isdisplay(self, element):
        """
        元素是否可见
        """
        flag = element.is_displayed
        if flag:
            return element
        else:
            return False

    def get_element(self, info):
        by, value = self.get_local_element(info)
        try:
            if by == "id" or 'name' or 'class' or 'css_selector' or 'link_text' or 'xpath':
                element = self.driver.find_element(by, value)
            else:
                element = self.driver.find_element(by, value)
        except:
            # self.error_png()
            return None
        return self.element_isdisplay(element)

    def get_elements(self, info):
        element_list = []
        by, value = self.get_local_element(info)
        if by == "id":
            elements = self.driver.find_elements_by_id(value)
        elif by == "name":
            elements = self.driver.find_elements_by_name(value)
        elif by == "class":
            elements = self.driver.find_elements_by_class_name(value)
        elif by == "css":
            elements = self.driver.find_elements_by_css_selector(value)
        else:
            elements = self.driver.find_elements_by_xpath(value)
        for element in elements:
            if not self.element_isdisplay(element):
                continue
            else:
                element_list.append(element)
        return elements

    def get_level_element(self, info_level, node_info):
        """
        层级定位
        父节点
        找子节点
        """
        element = self.get_element(info_level)
        node_by, node_value = node_info
        if not element:
            return False
        if node_by == 'id':
            node_element = element.find_element_by_id(node_value)
        elif node_by == "name":
            node_element = element.find_element_by_name(node_value)
        elif node_by == "class":
            node_element = element.find_element_by_class_name(node_value)
        elif node_by == "css":
            node_element = element.find_element_by_css_selector(node_value)
        elif node_by == "link":
            node_element = element.find_element_by_link_text(node_value)
        else:
            node_element = element.find_element_by_xpath(node_value)
        return self.element_isdisplay(node_element)

    def get_list_element(self, info, index):
        """
        通过list定位元素
        """
        elements = self.get_elements(info)
        len(elements)
        if len(elements) < index:
            return None
        return elements[index]

    def send_value(self, info, key):
        element = self.get_element(info)
        if not element:
            print("未找到元素，无法进行输入")
        else:
            if element is not None:
                element.send_keys(key)
            else:
                print("未找到元素，定位元素失败")

    def clear_element(self, info):
        element = self.get_element(info)
        if element:
            if element is not None:
                element.clear()
            else:
                print('未找到元素，无法清空')
        else:
            return None

    def click_element(self, info):
        element = self.get_element(info)
        if element:
            if element is not None:
                element.click()
            else:
                print("定位元素未找到！")
        else:
            return None

    def check_box(self, info, check):  # 复选框
        element = self.get_element(info)
        if element:
            flag = element.is_selected()  # 判断元素是否选中
            if flag:  # 选中元素
                if check != "check":  # 不需要选中
                    self.click_element(info)
            else:
                if check == "check":  # 需要选中
                    self.click_element(info)
        else:
            print("不可选中，元素不可见")

    def get_local_element(self, info):
        """
        拆分配置文件，返回by，local
        """
        data = read_ini.get_value(info)
        data_info = data.split(">")
        by = data_info[0]
        local = data_info[1]
        return by, local

    def get_selected(self, info, value, index=None):
        """
        通过index获取selected，然后选择selected
        下拉框为select标签
        """
        if index is not None:
            selected_element = self.get_list_element(info, index)
        else:
            selected_element = self.get_element(info)
        Select(selected_element).select_by_index(value)

    def upload_file(self, file_name):
        """
        非input上传文件
        """
        pykey = PyKeyboard()
        pykey.type_string(file_name)
        pykey.tap_key(pykey.enter_key)

    def action_member(self, info):
        """
        移动鼠标到某个元素上
        """
        element = self.get_element(info)
        ActionChains(self.driver).move_to_element(element).perform()

    def download_file(self, info):
        """
        下载文件
        """
        self.click_element(info)

    def js_calendar(self, info):
        """
        执行js代码函数
        """
        self.get_local_element(info)
        local = self.get_local_element(info)
        by = local[0]
        value = local[1]
        if by == "id":
            by_key = "getElementById"
            js = 'document.%s("%s").removeAttribute("readonly")' % (by_key, value)  # removeAttribute 删除属性
        else:
            by_key = "getElementsByClassName"
            js = 'document.%s("%s")[1].removeAttribute("readonly")' % (by_key, value)
        self.driver.execute_script(js)  # execute_script 执行脚本

    def calendar(self, info, value):
        """
        判断日历是否是只读属性，并执行
        """
        element = self.get_element(info)
        try:
            element.__getattribute__("readonly")
            self.js_calendar(info)
        except:
            print("不是只读属性的日历")
        element.clear()
        self.send_value(info, value)

    def scroll_get_element(self, list_info, title_name):
        """
        通过滑动滚动条，查找元素
        """
        element_list = self.get_elements(list_info)
        js = "document.documentElement.scrollTop=500"
        t = True
        while t:
            for element in element_list:
                name = element.find_element_by_tag_name("p").text
                if name in title_name:
                    element.click()
                    t = False
            self.driver.execute_script(js)

    def sceoll_element(self, info, px):
        """
        滑动px像素
        """
        js = "document.documentElement.scrollTop={}".format(px)
        t = True
        while t:
            try:
                self.get_element(info)
                t = False
            except:
                self.driver.execute_script(js)

    def img_png(self, filename):
        """
        截图
        """
        return self.driver.get_screenshot_as_file(filename)

    def save_png(self):
        """
        以时间戳为文件名截图
        """
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        pit_path = "/Users/xiachengpeng/PycharmProjects/pythonProject/picture/" + now_time + '.png'
        self.driver.get_screenshot_as_file(pit_path)
        return pit_path

    def error_png(self):
        """
        以时间戳为文件名截图错误信息
        """
        error_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        pit_path = "/Users/xiachengpeng/PycharmProjects/pythonProject/picture/" + "error" + error_time + '.png'
        self.driver.get_screenshot_as_file(pit_path)
        return pit_path

    def time_log(self, path=None):
        """
        以时间戳命名文件的日志
        """
        path_log = self.get_os(path)
        log_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        log_path = path_log + log_time + '.log'
        return log_path

    def get_picture(self, info):
        """
        截取验证码
        """
        file_name = self.save_png()
        code_element = self.get_element(info)
        left = code_element.location["x"]
        top = code_element.location["y"] + 140
        right = code_element.size["width"] + left
        height = code_element.size["height"] + top + 5
        img = Image.open(file_name)
        time.sleep(3)
        out = img.resize((1440, 878), Image.ADAPTIVE)
        out.save(file_name)
        image = out.crop((left, top, right, height))
        image.save(file_name)
        time.sleep(2)
        return file_name

    def code_online(self, file_name):
        """
        通过第三方API识别验证码
        https://route.showapi.com/184-4
        """
        r = ShowapiRequest("http://route.showapi.com/184-4", "509641", "54234cfed4a1478b90cb4e04f23d086e")
        r.addFilePara("image", file_name)
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        res = r.post()
        code_text = res.json()["showapi_res_body"]["Result"]
        time.sleep(1)
        return code_text

    def code_base64(self, file_name):
        """
        通过第三方API识别验证码
        base64转码识别
        """
        r = ShowapiRequest("http://route.showapi.com/932-2", "509641", "54234cfed4a1478b90cb4e04f23d086e")
        r.addFilePara("image", file_name)
        r.addBodyPara("length", "5")
        r.addBodyPara("specials", "false")
        r.addBodyPara("secure", "false")
        res = r.post()
        code_text = res.json()["showapi_res_code"]["code"]
        time.sleep(2)
        return code_text

    def get_range_user(self):
        """
        生成随机用户名
        """
        user_name = "".join(random.sample("1234567890abcdefg", 10))  # "".join() 表示将后面的列表转换为字符串
        return user_name

    def get_os(self, path=None):
        if path == '工程目录':
            file_path = os.path.dirname(os.path.dirname((os.getcwd())))
        else:
            file_path = os.getcwd()
        return file_path

    def sleep_time(self):
        time.sleep(2)

    def close_driver(self):
        self.driver.close()


selenium_driver = SeleniumDriver()
# selenium_driver.open_browser('chrome')
# selenium_driver.handle_window("max")
# selenium_driver.get_url("http://www.5itest.cn/register?goto=/")
# selenium_driver.send_value("user_path", 'test')
# sp = selenium_driver.get_picture("re")
# selenium_driver.close_driver()
# sm.main()
