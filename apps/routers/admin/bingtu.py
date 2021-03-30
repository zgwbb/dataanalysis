from apps.models import mydb
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
from functools import reduce

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


# Statistics = []
thisset = set()
life = 0
science = 0
shaoer = 0
original_edition = 0
Self_Improvement = 0
jisji = 0
jinying = 0
yishu = 0
rwen = 0
zazhi = 0
xiaoshuo = 0
jiaoyu = 0
my_col = mydb['Book_Info']
email_record = []
# 去重
email_record1 = my_col.find()
for i in email_record1:
    email_record.append({"标题":i["标题"],"类型": i["类型"], "总评数": i["总评数"]})
run_function = lambda x, y: x if y in x else x + [y]
email_record = reduce(run_function, [[], ] + email_record)
print(len(email_record))
for i in email_record:
    thisset.add(i["类型"])
    if i["类型"] == '生活':
        life = life + i["总评数"]
    elif i["类型"] == '科技':
        science = science + i["总评数"]
    elif i["类型"] == '原版图书':
        original_edition = original_edition + i["总评数"]
    elif i["类型"] == '励志与成功':
        Self_Improvement = Self_Improvement + i["总评数"]
    elif i["类型"] == '教育':
        jiaoyu = jiaoyu + i["总评数"]
    elif i["类型"] == '小说文学':
        xiaoshuo = xiaoshuo + i["总评数"]
    elif i["类型"] == '杂志期刊':
        zazhi = zazhi + i["总评数"]
    elif i["类型"] == '人文科学':
        rwen = rwen + i["总评数"]
    elif i["类型"] == '艺术/摄影':
        yishu = yishu + i["总评数"]
    elif i["类型"] == '经营':
        jinying = jinying + i["总评数"]
    elif i["类型"] == '计算机与互联网':
        jisji = jisji + i["总评数"]
    else:
        shaoer = shaoer + i["总评数"]
Statistics = {'生活':life, '科技':science, '原版图书':original_edition, '励志与成功':Self_Improvement,
       '教育':jiaoyu, '小说文学':xiaoshuo, '杂志期刊':zazhi, '人文科学':rwen,
       '艺术/摄影':yishu, '经营':jinying, '计算机与互联网':jisji, '少儿':shaoer}
labels = list(Statistics.keys())
sizes = list(Statistics.values())
print(sizes)
print(labels)
# print(thisset)
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

plt.pie(sizes,  labels=labels,
        autopct='%0.3f%%', shadow=True, startangle=90)

# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

plt.savefig('D:\pie.png')
plt.show()
