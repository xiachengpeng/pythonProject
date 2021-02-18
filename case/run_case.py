# import unittest
#
#
# class RunCase(unittest.TestCase):
#     """
#     运行多个文件的case
#     """
#
#     def test_case01(self):
#         case_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取当前根目录文件
#         suite = unittest.defaultTestLoader.discover(case_path, 'unittest_*.py')
#         unittest.TextTestRunner().run(suite)
#
#
# if __name__ == "__main__":
#     unittest.main()

# case_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(type(case_path))
from base import ShowapiRequest
from base.open_driver import selenium_driver
from PIL import Image
import time


# selenium_driver.handle_window("max")
# selenium_driver.get_url("http://www.5itest.cn/register?goto=/")
# file_name = selenium_driver.get_picture('re')


class CodeText:

    def get_picture(self, info):
        """
        截取验证码
        """
        file_name = selenium_driver.save_png()
        code_element = selenium_driver.get_element(info)
        left = code_element.location["x"]
        top = code_element.location["y"] + 140
        right = code_element.size["width"] + left
        height = code_element.size["height"] + top + 5
        img = Image.open(file_name)
        time.sleep(3)
        out = img.resize((1440, 875), Image.ADAPTIVE)
        out.save(file_name)
        image = out.crop((left, top, right, height))
        image.save(file_name)
        time.sleep(2)
        return file_name

    def code_api(self, file_name):
        r = ShowapiRequest("http://route.showapi.com/932-2", "509641", "54234cfed4a1478b90cb4e04f23d086e")
        r.addFilePara("image", file_name)
        r.addBodyPara("length", "5")
        r.addBodyPara("specials", "false")
        r.addBodyPara("secure", "false")
        res = r.post()
        code_text = res.json()["showapi_res_body"]["code"]
        return code_text


selenium_driver.handle_window('max')
selenium_driver.get_url("http://www.5itest.cn/register")
ct = CodeText()
file_name = ct.get_picture('re')
ct.code_api(file_name)
