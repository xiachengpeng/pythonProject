from handles.register_handle import RegisterHandle
import sys
import os

curPath = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(curPath)


class RegisterBusiness:
    """
    执行操作
    """

    def __init__(self):
        self.register_h = RegisterHandle()

    def user_base(self, email, name, password, file_name):
        self.register_h.send_email(email)
        self.register_h.send_name(name)
        self.register_h.send_password(password)
        self.register_h.send_code(file_name)
        self.register_h.click_button()
        self.register_h.get_register_button()

    def register_success(self):
        if self.register_h.get_register_button() is None:
            return True
        else:
            return False

    def register_email_error(self, email, name, password, file_name):
        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text("email_error") is None:
            print('邮箱校验不成功')
            return True
        else:
            return False

    def register_function(self, email, name, password, file_name, assertcode):
        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text(assertcode) is None:
            print('邮箱校验不成功')
            return True
        else:
            return False

    def register_name_error(self, email, name, password, file_name):
        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text("name_error") is None:
            print('用户名校验不成功')
            return True
        else:
            return False

    def register_password_error(self, email, name, password, file_name):
        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text("password_error") is None:
            print('密码校验不成功')
            return True
        else:
            return False

    def register_code_error(self, email, name, password, file_name):
        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text("code_error") is None:
            print('验证码校验不成功')
            return True
        else:
            return False

    def register_succes(self, email, name, password, file_name):
        self.user_base(email, name, password, file_name)
