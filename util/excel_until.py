import xlrd
from xlutils.copy import copy


class ExcelUtil:
    """
    excel操作类
    """

    def __init__(self, excel_path=None, index=None):
        if excel_path is None:
            self.excel_path = "/Users/xiachengpeng/PycharmProjects/pythonProject/coding/testcase.xls"
        else:
            self.excel_path = excel_path
        if index is None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)  # 打开Excel文件
        self.table = self.data.sheets()[index]  # 获取表内容

    def get_data(self):
        """
        获取Excel数据，将每一行的数据添加到list里面
        """
        result = []
        rows = self.get_rows()
        if rows is not None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        else:
            return None

    def get_rows(self):
        """
        获取Excel行数
        """
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    def get_col_value(self, row, col):
        """
        获取单元格数据
        """
        if self.get_rows() >= row:
            data = self.table.cell(row, col).value
            return data
        return False

    def write_excel(self, row, col, value):
        """
        写入Excel数据
        """

        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)  # 复制
        write_data.get_sheet(0).write(row, col, value)
        write_data.save(self.excel_path)


# eu = ExcelUtil('/Users/xiachengpeng/Desktop/keyword.xlsx')
# method = eu.get_col_value(3, 4)
# send_value = eu.get_col_value(4, 5)
# handle_value = eu.get_col_value(5, 6)
# print(method)