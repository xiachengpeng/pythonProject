import sys

sys.path.append('/Users/xiachengpeng/PycharmProjects/pythonProject')
from business.register_business import RegisterBusiness
from base.open_driver import selenium_driver
from log.log_user import UserLog
import unittest
import HTMLTestRunner
import time
import os


class FirstCase(unittest.TestCase):
    """
    case层
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = UserLog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.register_b = RegisterBusiness()
        self.logger.info("this is textt")
        # self.file_name = selenium_driver.get_picture('re')
        # self.code_text = selenium_driver.code_base64(self.file_name)

    def tearDown(self):
        time.sleep(2)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                error_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                case_error_path = os.path.join(error_path + "/report/" + case_name + '.png')
                selenium_driver.img_png(case_error_path)
        selenium_driver.close_driver()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.log.close_log()

    # 邮箱、用户名、密码、验证码、错误信息元素、错误提示信息
    def test_register_email_error(self):
        email_error = self.register_b.register_email_error('qweqwe', '程柔位', '123456', 'code1')
        self.assertFalse(email_error)  # 断言是否为false

    def test_register_username_error(self):
        name_error = self.register_b.register_name_error('qwe@123.com', '1', '123456', 'code1')
        self.assertFalse(name_error)

    def test_register_password_error(self):
        password_error = self.register_b.register_password_error('qwe@123.com', 'chengtouwei', '1234', 'code1')
        self.assertFalse(password_error)

    def test_register_code_error(self):
        code_error = self.register_b.register_code_error('qwe@123.com', 'chengtouwei', '123456', 'code1')
        self.assertFalse(code_error)

    def test_register_success(self):
        success = self.register_b.register_succes('qwe@123.com', 'chengtouwei', '123456', 'code1')
        self.assertTrue(success)


if __name__ == '__main__':
    # f_path = os.path.dirname((os.getcwd()))
    file_path = os.path.join('/Users/xiachengpeng/PycharmProjects/pythonProject' + "/report/" + 'first_case.html')
    print(file_path)
    f = open(file_path, "wb")
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_register_email_error'))
    suite.addTest(FirstCase('test_register_username_error'))
    suite.addTest(FirstCase('test_register_password_error'))
    suite.addTest(FirstCase('test_register_code_error'))
    # unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="this is first report", description=u"这个是测试报告",
                                           verbosity=2)
    runner.run(suite)
