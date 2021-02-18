import HTMLTestRunner
import os
import time
import unittest
import ddt
from base.open_driver import selenium_driver
from business.register_business import RegisterBusiness
from util.excel_until import ex

data = ex.get_data()


# 邮箱、用户名、密码、验证码、错误信息元素、错误提示信息
@ddt.ddt()
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.register_b = RegisterBusiness()
        # self.file_name = selenium_driver.get_picture('re')

    def tearDown(self):
        time.sleep(2)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                error_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
                case_error_path = os.path.join(error_path + "/report/" + case_name + '.png')
                selenium_driver.img_png(case_error_path)
    '''
    @ddt.data(
        ["123", 'anmuxi', '12345', 'code', 'user_email_error'],
        ["@123.com", 'anmuxi', '12345', 'code', 'user_email_error'],
        ["123@123.com", 'anmuxi', '12345', 'code', 'user_email_error']
    )
    @ddt.unpack
    '''
    @ddt.data(*data)
    def test_register_case(self, data):
        email, name, password, file_name, assertcode = data
        email_error = self.register_b.register_function(email, name, password, file_name, assertcode)
        self.assertFalse(email_error)  # 断言是否为false


if __name__ == '__main__':
    f_path = os.path.dirname(os.path.dirname((os.getcwd())))
    file_path = os.path.join(f_path + "/report/" + 'first_case.html')
    f = open(file_path, "wb")
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="this is first report", description=u"这个是测试报告",
                                           verbosity=2)
    runner.run(suite)
