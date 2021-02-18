from page.register_page import RegisterPage


class RegisterHandle:
    """
    操作层
    """

    def __init__(self):
        self.register_p = RegisterPage()

    def send_email(self, email):
        self.register_p.get_email_element().send_keys(email)

    def send_name(self, name):
        self.register_p.get_name_element().send_keys(name)

    def send_password(self, password):
        self.register_p.get_password_element().send_keys(password)

    def send_code(self, file_name):
        # code_text = selenium_driver.code_base64(file_name)
        self.register_p.get_code_element().send_keys(file_name)

    def get_user_text(self, info):
        try:
            if info == "user_email_error":
                text = self.register_p.get_email_error().text
            elif info == "user_name_error":
                text = self.register_p.get_name_error().text
            elif info == "user_password_error":
                text = self.register_p.get_password_error().text
            else:
                text = self.register_p.get_code_error().text
        except:
            text = None
        return text

    def click_button(self):
        self.register_p.get_button().click()

    def get_register_button(self):
        return self.register_p.get_button().text
