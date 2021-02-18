# a = ["xia", "cheng", "peng"]
# a.reverse()
# print(a)


# def rotate(input, d):
#     Lfirst = input[0: d]
#     Lsecond = input[d:]
#     Rfirst = input[0: len(input) - d]
#     Rsecond = input[len(input) - d:]
#
#     print("头部切片翻转 : ", (Lsecond + Lfirst))
#     print("尾部切片翻转 : ", (Rsecond + Rfirst))
#
#
# if __name__ == "__main__":
#     input = 'Runoob'
#     d = 2  # 截取两个字符
#     rotate(input, d)

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('{}x{}={} '.format(j, i, i*j), end='')
#     print("")
import xlrd
import openpyxl
import os
# import pandas as pd
#
# #
# # class ExcelUtil:
# #     def __init__(self, excel_path=None, index=None):
# #         # if excel_path is None:
# #         #     excel_path = "/Users/xiachengpeng/PycharmProjects/pythonProject/coding/testcase.xls"
# #         # if index is None:
# #         #     index = 0
# #         self.data = pd.read_excel("/Users/xiachengpeng/PycharmProjects/pythonProject/coding/testcase.xls", header=None)
# #         print(self.data)
# #
# #
# # ex = ExcelUtil()
# data = pd.read_excel("/Users/xiachengpeng/PycharmProjects/pythonProject/coding/testcase.xls", header=None)
# print(data)
f_path = os.path.dirname(os.path.dirname((os.getcwd())))
print(f_path)