from apps.models import mydb
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
import operator
from functools import reduce
import itertools
import time
from operator import itemgetter
from itertools import groupby

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
data1 = []
pinglun = []
my_col = mydb['Book_Info']



email_record = my_col.find()
for i in email_record:
    # 对于每个类别的数据量进行排序
    data1.append({"商品id": i["商品id"], "标题": i['标题'],
                  "评价": i['评价'],"总评数":i['总评数'],"类型":i["类型"]})
# 去重
run_function = lambda x, y: x if y in x else x + [y]
data1= reduce(run_function, [[], ] + data1)
list2 = sorted(data1, key=operator.itemgetter('总评数'), reverse=True)
# for i in list2:
#     print(i['评价'])
leixin = []
all_data = []
for i in list2:
    strlist = i['评价'].split('，')
    for j in strlist:
        if j == '':
            strlist.remove(j)
    pinglun.append(strlist)
    leixin.append(i["类型"])
    all_data.append({"类型":i['类型'],"评价": strlist})
all_data = sorted(all_data, key=itemgetter('类型'))
res = dict((k, list(g)) for k, g in itertools.groupby(all_data, key=itemgetter('类型')))
# print(res)
rwords=[brand for drink in pinglun for brand in drink] #将列表扁平化
count={} #空元组
for item in rwords:
    count[item]=count.get(item,0)+1 #get 查找键 item
ciyu = {}
print(count)
for i in list(count.keys()):
    ciyu[i] = 0
count1 = {}
for item in leixin:
    count1[item]=count1.get(item,0)+1 #get 查找键 item
all_pinlun = []
for i in list(count1.keys()):
    all_haopindu = []
    for j in res[i]:
        all_haopindu =  all_haopindu + j['评价']
    dan_ciyu = {}  # 空元组
    for item1 in all_haopindu:
        dan_ciyu[item1] = dan_ciyu.get(item1, 0) + 1  # get 查找键 item
    for k in list(dan_ciyu.keys()):
        ciyu[k] = dan_ciyu[k]
    text = list(ciyu.values())
    all_pinlun.append({i:text})
    # print(ciyu)
all_data_zong = []
for i in all_pinlun:
    all_data_zong.append(list(i.values())[0])
for i in all_data_zong:
    print(i)
data_all_shuju = []
indicator = []
for i in list(count.keys()):
    indicator.append({"name": i, max: 100})
print(count1)
for i in range(len(all_data_zong)):
    print(type(all_data_zong[i][0]))
    data_all_shuju.append({"value":all_data_zong[i], "name":list(count1.keys())[i]})

# print(list(count.keys()))
# print(len(list(count.keys())))
# data_labels = np.array(list(count1.keys()))
# n = len(list(count.keys()))
# print(count.keys())
# print(count1.keys())
# radar_labels = np.array(list(count.keys()))    # 为了美观加了几个空格
# data=np.array(all_data_zong)
# angles=np.linspace(0, 2*np.pi, n, endpoint=False)       # 将360度平均分为n个部分（有endpoint=False分为6个部分，反之5个部分）
# # data=np.concatenate((data, [data[0]]))
# # angles=np.concatenate((angles, [angles[0]]))
# # radar_labels=np.concatenate((radar_labels, [radar_labels[0]]))
# # data_labels=np.concatenate((data_labels, [data_labels[0]]))
# fig = plt.figure(facecolor='white', figsize=(10,8))    # 绘制全局绘图区域
# plt.subplot(111, polar=True)    # 绘制一个1行1列极坐标系子图，当前位置为1
# # 拼接数据首尾，使图形中线条封闭
#
#
# # plt.figtext(0.52,0.95,'霍兰德人格分析',ha='center',size=20)   #放置标题 ，ha是horizontalalignment（水平对齐方式）的缩写
# plt.thetagrids(angles*180/np.pi, radar_labels)       # 放置属性（radar_labels）
# plt.plot(angles, data, 'o-', linewidth=1.5, alpha=0.2)      # 连线，画出不规则六边形
# plt.fill(angles, data, alpha=0.25)        # 填充，alpha是透明度（自己的实践理解）
# legend=plt.legend(data_labels, loc=(0.94, 0.80), labelspacing=0.1)    # 放置图注（右上角）
# plt.setp(legend.get_texts(), fontsize='medium')
# plt.grid(True)    # 打开坐标网格
# plt.show()       # 显示
# fig.savefig('雷达图.jpg', dpi=500)
