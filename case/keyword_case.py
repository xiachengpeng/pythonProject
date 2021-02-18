from util.excel_until import ExcelUtil
from base.open_driver import SeleniumDriver


class KeyWordCase:

    def __init__(self):
        self.selenium_driver = SeleniumDriver()

    def run_main(self):
        eu = ExcelUtil('/Users/xiachengpeng/Desktop/keyword.xlsx')
        case_rows = eu.get_rows()
        if case_rows:
            for i in range(1, case_rows):
                is_run = eu.get_col_value(i, 3)
                if is_run == "是":
                    method = eu.get_col_value(i, 4)
                    send_value = eu.get_col_value(i, 5)
                    handle_value = eu.get_col_value(i, 6)
                    except_result_method = eu.get_col_value(i, 7)
                    except_result = eu.get_col_value(i, 8)
                    self.run_method(method, handle_value, send_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == "text":
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                eu.write_excel(i, 9, "pass")
                            else:
                                eu.write_excel(i, 9, "fail")
                        elif except_value[0] == "element":
                            result = self.run_method(except_result_method, except_value[1])
                            if result:
                                eu.write_excel(i, 9, 'pass')
                            else:
                                eu.write_excel(i, 9, 'fail')
                    else:
                        print('预期结果为空')

    def get_except_result_value(self, data):
        """
        获取预期结果值
        """
        return data.split("=")

    def run_method(self, method, send_value='', handle_value=''):
        method_value = getattr(self.selenium_driver, method)
        if send_value == '' and handle_value != '':
            result = method_value(handle_value)
        elif send_value == '' and handle_value == '':
            result = method_value()
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        else:
            result = method_value(handle_value, send_value)
        return result


if __name__ == "__main__":
    kw = KeyWordCase()
    kw.run_main()
