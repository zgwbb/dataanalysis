from apps.models import mydb
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
from functools import reduce

# 叠图
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
all_data1 = []
my_col = mydb['Book_Info']
email_record = my_col.find()
for i in email_record:
    all_data1.append(i['出版社'])
data_dict = {}
for key in all_data1:
    data_dict[key] = data_dict.get(key,0) + 1
data_dict = sorted(data_dict.items(), key=lambda item:item[1],reverse=True)
chubanshe = []
xdata = []
for i in data_dict[0:11]:
    xdata.append(i[0])
    chubanshe.append({"出版社": i[0]})
# print(chubanshe)
# 多条件查询
# all_chubanshe = my_col.find({ "$or": chubanshe})
all_leixing = []
for i in chubanshe:
    all_chubanshe = my_col.find(i)
    leixing = []
    for j in all_chubanshe:
        leixing.append(j['类型'])
    all_leixing.append(i)
    all_leixing.append(leixing)
print(len(all_leixing))
jishu = all_leixing[::2]
oushu = all_leixing[1::2]
tongji_oushu = []
for i in oushu:
    count = {}  # 空元组
    for item in i:
        count[item] = count.get(item, 0) + 1  # get 查找键 item
    count = sorted(count.items(), key=lambda item: item[1], reverse=True)
    tongji_oushu.append(count)
data = []
for i in tongji_oushu:
    for j in i:
        data.append(j[0])
data = ['经营', '人文科学', '少儿', '小说文学', '艺术/摄影', '教育', '科技', '生活', '励志与成功', '计算机与互联网']
print(xdata)
series = [
    {
        "name": '经营',
        "type": 'bar',
        "emphasis": {
            "focus": 'series'
        },
        "data": [13, 30, 15, 0, 17, 2, 0, 2, 0,0]
    },
    {
        "name": '人文科学',
        "type": 'bar',
        "emphasis": {
            "focus": 'series'
        },
        "data": [2, 1, 8, 0, 3,  2, 0, 0, 7,0]
    },
    {
        "name": '少儿',
        "type": 'bar',
        "emphasis": {
            "focus": 'series'
        },
        "data": [0, 0, 20, 0, 0,  0, 0, 1, 0,0]
    },
{
        "name": '小说',
        "type": 'bar',
        "emphasis": {
            "focus": 'series'
        },
        "data": [0, 0, 3, 0, 1, 0, 0, 21, 3,0]
    },
{
        "name": '艺术/摄影',
        "type": 'bar',
        "emphasis": {
            "focus": 'series'
        },
        "data": [11, 0, 4, 0, 23, 2, 31, 0, 2,0]
    },
{
        "name": '教育',
        "type": 'bar',
        "emphasis": {
            "focus": 'series'
        },
        "data": [6, 0, 0, 37, 0, 0, 0, 0, 0, 0]
    },
{
        "name": '科技',
        "type": 'bar',
        "emphasis": {
            "focus": 'series'
        },
        "data": [9, 6, 9, 0, 4, 1, 0, 1, 0,0]
    },
{
        "name": '生活',
        "type": 'bar',
        "emphasis": {
            "focus": 'series'
        },
        "data": [3, 2, 16, 0, 10,0, 0, 4, 2,0]
    },
{
        "name": '励志与成功',
        "type": 'bar',
        "emphasis": {
            "focus": 'series'
        },
        "data": [10, 16, 15, 0, 12, 6, 0, 0, 15,0]
    },
{
        "name": '计算机与互联网',
        "type": 'bar',
        "emphasis": {
            "focus": 'series'
        },
        "data": [55, 48, 0, 0, 0, 21, 0, 0, 0,0]
    },
{
        "name": '原版图书',
        "type": 'bar',
        "emphasis": {
            "focus": 'series'
        },
        "data": [0, 0, 0, 0, 0, 0, 0, 0, 0,27]
    },
]
for i in range(len(tongji_oushu)):
    print({jishu[i]['出版社']:tongji_oushu[i]})

