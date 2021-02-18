from base.open_driver import selenium_driver


class RegisterPage:
    def __init__(self):
        self.selenium_d = selenium_driver
        self.selenium_d.open_browser('chrome')
        self.selenium_d.handle_window('max')
        self.selenium_d.get_url("http://www.5itest.cn/register")

    def get_email_element(self):
        return self.selenium_d.get_element('user_email')

    def get_name_element(self):
        return self.selenium_d.get_element("user_name")

    def get_password_element(self):
        return self.selenium_d.get_element("password")

    def get_code_element(self):
        return self.selenium_d.get_element("register_code")

    def get_button(self):
        return self.selenium_d.get_element("register_button")

    def get_email_error(self):
        return self.selenium_d.get_element("user_email_error")

    def get_name_error(self):
        return self.selenium_d.get_element("user_name_error")

    def get_password_error(self):
        return self.selenium_d.get_element("user_password_error")

    def get_code_error(self):
        return self.selenium_d.get_element("user_code_error")
