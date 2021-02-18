# coding=utf-8

# 生成年月日时分秒时间
# picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
# print(picture_time)
# print(directory_time)
# # 打印文件目录
# print(os.getcwd())
# # 获取到当前文件的目录，并检查是否有 directory_time 文件夹，如果不存在则自动新建 directory_time 文件
# try:
#     File_Path = os.getcwd() + '\\' + directory_time + '\\'
#     if not os.path.exists(File_Path):
#         os.makedirs(File_Path)
#         print("目录新建成功：%s" % File_Path)
#     else:
#         print("目录已存在！！！")
# except BaseException as msg:
#     print("新建目录失败：%s" % msg)
#
# driver = webdriver.Chrome()
# driver.get("https://baidu.com/")
# try:
#     url = driver.save_screenshot('.\\' + directory_time + '\\' + picture_time + '.png')
#     print("%s ：截图成功！！！" % url)
# except BaseException as pic_msg:
#     print("截图失败：%s" % pic_msg)
# time.sleep(2)
# driver.quit()
r = ShowapiRequest("https://route.showapi.com/184-4", "509641", "54234cfed4a1478b90cb4e04f23d086e")
r.addFilePara("image", "/Users/xiachengpeng/PycharmProjects/pythonProject/picture/2021-01-12 21:14:52.png")
r.addBodyPara("length", "5")
r.addBodyPara("specials", "false")
r.addBodyPara("secure", "true")
res = r.post()
code_text = res.json()["showapi_res_body"]
print(code_text)

res = r.post()
print(res.text)