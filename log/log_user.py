import logging
import os
import datetime


class UserLog:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)  # 设置日志等级

        # 控制台输出日志
        # console = logging.StreamHandler()
        # logger.addHandler(console)
        # logger.debug("test1234")
        # console.close()
        # logger.removeHandler(console)

        # 文件名称
        base_path = os.path.dirname(os.path.abspath(__file__))
        log_path = os.path.join(base_path, 'logs')
        log_file = datetime.datetime.now().strftime("%Y-%m-%d" + '.log')
        log_name = log_path + '/' + log_file
        # 文件输出日志
        self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s------> %(message)s')  # 格式化日志文件
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger

    def close_log(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


ul = UserLog()
ul.get_log()
ul.logger.debug("text")
ul.close_log()
