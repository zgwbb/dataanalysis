from apps.models import mydb
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
from functools import reduce

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

thisset = set()
life = []
science = []
shaoer = []
original_edition = []
Self_Improvement = []
jisji = []
jinying = []
yishu = []
rwen = []
zazhi = []
xiaoshuo = []
jiaoyu = []
my_col = mydb['Book_Info']
data1 = []
all_data = []
all_data1 = []
email_record = my_col.find()
for i in email_record:
    all_data1.append({"标题":i["标题"],"类型": i["类型"], "折扣": i['折扣']})
    if i["类型"] == '生活':
        life.append({"标题":i["标题"],"类型": i["类型"], "折扣": i['折扣']})
    elif i["类型"] == '科技':
        science.append({"标题":i["标题"],"类型": i["类型"], "折扣": i['折扣']})
    elif i["类型"] == '原版图书':
        original_edition.append({"标题":i["标题"],"类型": i["类型"], "折扣": i['折扣']})
    elif i["类型"] == '励志与成功':
       Self_Improvement.append({"标题":i["标题"],"类型": i["类型"], "折扣": i['折扣']})
    elif i["类型"] == '教育':
        jiaoyu.append({"标题":i["标题"],"类型": i["类型"], "折扣": i['折扣']})
    elif i["类型"] == '小说文学':
        xiaoshuo.append({"标题":i["标题"],"类型": i["类型"], "折扣": i['折扣']})
    elif i["类型"] == '杂志期刊':
        zazhi.append({"标题":i["标题"],"类型": i["类型"], "折扣": i['折扣']})
    elif i["类型"] == '人文科学':
        rwen.append({"标题":i["标题"],"类型": i["类型"], "折扣": i['折扣']})
    elif i["类型"] == '艺术/摄影':
        yishu.append({"标题":i["标题"],"类型": i["类型"], "折扣": i['折扣']})
    elif i["类型"] == '经营':
        jinying.append({"标题":i["标题"],"类型": i["类型"], "折扣": i['折扣']})
    elif i["类型"] == '计算机与互联网':
        jisji.append({"标题":i["标题"],"类型": i["类型"], "折扣": i['折扣']})
    else:
        shaoer.append({"标题":i["标题"],"类型": i["类型"], "折扣": i['折扣']})
print(len(science))
run_function = lambda x, y: x if y in x else x + [y]
life = reduce(run_function, [[], ] + life)
Self_Improvement = reduce(run_function, [[], ] + Self_Improvement)
science = reduce(run_function, [[], ] + science)
original_edition = reduce(run_function, [[], ] +  original_edition)
jiaoyu = reduce(run_function, [[], ] + jiaoyu)
xiaoshuo = reduce(run_function, [[], ] + xiaoshuo)
zazhi = reduce(run_function, [[], ] + zazhi)
rwen = reduce(run_function, [[], ] + rwen)
shaoer = reduce(run_function, [[], ] + shaoer)
jisji = reduce(run_function, [[], ] + jisji)
jinying = reduce(run_function, [[], ] + jinying)
yishu = reduce(run_function, [[], ] + yishu)
print(len(science))
print(len(all_data))
zkxq = []
all_data= [life,Self_Improvement,science,original_edition,jiaoyu,xiaoshuo,zazhi,rwen,shaoer,jisji,jinying,yishu]
# 分析各个类别的折扣数据
for i in all_data:
    two = 0
    t_f = 0
    f_x = 0
    max_x = 0
    for j in i:
        if float(j['折扣']) <= float(0.2):
            two = two + 1
        elif float(j['折扣']) > float(0.2) and float(j['折扣']) <= float(0.4):
            t_f = t_f + 1
        elif float(j['折扣']) > float(0.4) and  float(j['折扣']) <= float(0.6) :
            f_x = f_x + 1
        else:
            max_x = max_x +1
    zkxq.append({'product':j['类型'],'≤2 折':two,"2 －4 折": t_f,"4 －6 折":f_x,"＞6 折":max_x})
for i in zkxq:
    print(i)
# 全部类型书的折扣信息
all_two = 0
all_t_f = 0
all_f_x = 0
all_max_x = 0
all_data1 = reduce(run_function, [[], ] + all_data1)
print(len(all_data1))
for j in all_data1:
    if float(j['折扣']) <= float(0.2):
        all_two = all_two + 1
    elif float(j['折扣']) > float(0.2) and float(j['折扣']) <= float(0.4):
        all_t_f = all_t_f + 1
    elif float(j['折扣']) > float(0.4) and  float(j['折扣']) <= float(0.6) :
        all_f_x = all_f_x + 1
    else:
        all_max_x = all_max_x +1
print("---------------输出总的折扣信息----------------------")
print({'≤2 折':all_two,"2 －4 折": all_t_f,"4 －6 折":all_f_x,"＞6 折":all_max_x})

all_zhekouxinxi = {'≤2 折':all_two,"2 －4 折": all_t_f,"4 －6 折":all_f_x,"＞6 折":all_max_x}
waters = list(all_zhekouxinxi.keys())
buy_number = list(all_zhekouxinxi.values())

# 绘图
plt.bar(range(4), buy_number, align = 'center', color = 'steelblue', alpha = 0.8)
# 添加轴标签
plt.ylabel('书本的数量')
# 添加标题
plt.title('京东畅销榜图书折扣信息')
# 添加刻度标签
plt.xticks(range(4), waters)
# 设置Y轴的刻度范围
plt.ylim([0, 1000])
# 为每个条形图添加数值标签
for x,y in enumerate(buy_number):
    plt.text(x, y+100, '%s' %round(y,1), ha='center')
# 显示图形
plt.show()

