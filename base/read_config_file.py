import configparser


class ReadIni:
    def __init__(self, position=None, coding=None):
        """
        需要传入配置文件路径
        """
        if position is None:
            position = "/Users/xiachengpeng/PycharmProjects/pythonProject/coding/LocalElement.ini"
        if coding is None:
            self.coding = "element"
        else:
            self.coding = coding
        self.data = self.load_ini(position)

    def load_ini(self, position):  # position 位置
        cf = configparser.ConfigParser()
        cf.read(position)
        return cf

    def get_value(self, key):
        return self.data.get(self.coding, key)


read_ini = ReadIni()
