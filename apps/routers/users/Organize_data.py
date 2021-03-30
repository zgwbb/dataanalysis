import pandas as pd
import numpy as np
import random,json
import operator
import csv
from apps.models import mydb
import xlrd



my_col = mydb['Book_Info']
# IO = '京东图书数据1200.xlsx'

# 数据转换
# sheet = pd.read_excel('京东图书数据1200.xlsx',engine='openpyxl')
# # data=sheet.head()#默认读取前5行的数据
# # data=sheet.iloc[0].values#0表示第一行 这里读取数据并不包含表头，要注意哦！
# # print("读取指定行的数据：\n{0}".format(data))
# # print(type(data[15]))
# # 获取列数
# # print(sheet.shape[1])
# #  获取行数
# # print(sheet.shape[0])
# lange2 = []
# no_need_organize = ['少儿',"教育","小说文学","经营","励志与成功","艺术/摄影","科技","计算机与互联网","原版图书","杂志期刊","人文社科","生活"]
# shaoer = ['童书']
# jiaoyu = ['外语学习',"中小学教辅","大中专教材教辅","考试","字典词典/工具书"]
# xiaoshuo = ['小说','文学','青春文学','传记','动漫']
# jingying = ['管理','金融与投资','经济']
# rwensheke = ['历史','政治军事','心理学','法律','哲学宗教','国学古籍','国学/古籍','国学','古籍','社会科学','文化','哲学/宗教','政治/军事']
# shenghuo = ['育儿/家教','烹饪/美食','旅游地图','烹饪','美食','旅游/地图','育儿','家教','运动/健身',
#             '旅游','地图','婚恋与两性','家具','健身与保健','时尚美妆','体育运动','娱乐休闲','孕产/胎教','家居','养生/保健']
# yishu = ['艺术','摄影','绘画','音乐','书法']
# keji = ['科学与自然','工业技术','建筑','医学','电子与通信','科普读物','农业林业']
# yuanbantushu = ['英文进口图书','港台进口图书','日文进口图书','进口原版','港台图书']
# zazhi = ['杂志/期刊']
# for i in range(0, sheet.shape[0]):
#     data = sheet.iloc[i].values  # 0表示第一行 这里读取数据并不包含表头，要注意哦！
#     # print(data[2])
#     if  data[2]  in (no_need_organize) :
#         lange2.append(data[2])
#     elif data[2] in (jiaoyu):
#         lange2.append("教育")
#     elif data[2] in (xiaoshuo):
#         lange2.append('小说文学')
#     elif data[2] in (jingying):
#         lange2.append("经营")
#     elif data[2] in (rwensheke):
#         lange2.append("人文科学")
#     elif data[2] in (shenghuo):
#         lange2.append("生活")
#     elif data[2] in (keji):
#         lange2.append('科技')
#     elif data[2] in (yuanbantushu):
#         lange2.append("原版图书")
#     elif data[2] in (shaoer):
#         lange2.append('少儿')
#     elif data[2] in (zazhi):
#         lange2.append("杂志期刊")
#     elif data[2] in (yishu):
#         lange2.append("艺术/摄影")
#     else:
#         print(data[2])

# 数据数量分析

data1 = []
sheet1 = pd.read_excel('京东图书数据1200改3.xlsx',engine='openpyxl')
# for i in range(0, sheet1.shape[0]):
#     data = sheet1.iloc[i].values  # 0表示第一行 这里读取数据并不包含表头，要注意哦！
#     data1.append({"商品id": data[0],  "标题": data[1], "类型": data[2], "作者":data[3], "价格": data[4], "折扣":data[5],
#                   "出版社": data[6], "ISBN": data[7], "品牌":data[8], "包装": data[9], "出版时间":data[10],
#                   "用纸":data[11], "好评率": data[12], "好评度词":data[13], "总评数": data[14], "好评数":data[15], "差评数":data[16]})

# 把数据插入到书籍信息集合中
# data = xlrd.open_workbook('京东图书数据1200改3.xlsx')
# table = data.sheets()[0]
# # 读取excel第一行数据作为存入mongodb的字段名
# rowstag = table.row_values(0)
# nrows = table.nrows
# returnData = {}
#
#
# for i in range(1, nrows):
#     # 将字段名和excel数据存储为字典形式，并转换为json格式
#     returnData[i] = json.dumps(dict(zip(rowstag, table.row_values(i))))
#     # 通过编解码还原数据
#     returnData[i] = json.loads(returnData[i])
#     # print returnData[i]
#     my_col.insert_one(returnData[i])
#上传销售量前10的评论
list2 = sorted(data1, key=operator.itemgetter('数量'), reverse=True)
list2 = list2[:10]
# 销量前十的图书
num = 1
all_comment = []
for i in list2:
    book_name = i["书名"]
    i["书名"] = i["书名"] + ".csv"
    with open(i["书名"], 'r') as f:
        reader = csv.reader(f)
        # print(type(reader))
        for row in reader:
            all_comment.append(
                {"user_id": row[0],
            "comment_time": row[1],
            "all_comment": row[2]})
        my_col.insert_one({"title": book_name,
                           "details": all_comment})




# # 判断每本书的
# for i in range(0, sheet1.shape[0]):
#     data = sheet1.iloc[i].values  # 0表示第一行 这里读取数据并不包含表头，要注意哦！
#     data1.append(data[2])
# dict = {}
# for key in data1:
#     dict[key] = dict.get(key, 0) + 1
# print(dict)

# 对于每个类别的数据量进行排序
# del_data = []
# for i in range(0, sheet1.shape[0]):
#     data = sheet1.iloc[i].values  # 0表示第一行 这里读取数据并不包含表头，要注意哦！
#     data1.append({"商品id": data[0],  "书名": data[1], "类型": data[2], "数量": int(data[14])})
# for i in data1:
#     if i['类型'] == '杂志期刊':
#         del_data.append(i)
# list2 = sorted(del_data, key=operator.itemgetter('数量'), reverse=True)
# for i in list2:
#     print(i)




# dict = {}
# for key in data1:
#     dict[key] = dict.get(key, 0) + 1
# print(dict)
# print(len(lange2))
# with open('sampleList1.csv', 'r') as f1:
#     list1 = f1.readlines()
# for i in range(0, len(list1)):
#     list1[i] = list1[i].rstrip('\n')
# dict = {}
# for key in list1:
#     dict[key] = dict.get(key, 0) + 1
# print(dict)
# fileObject = open('sampleList1.csv', 'w')
# for ip in lange2:
#  fileObject.write(str(ip))
#  fileObject.write('\n')
# fileObject.close()