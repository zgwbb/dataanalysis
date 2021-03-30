from apps.models import mydb
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
import operator

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
data1 = []
pinglun = []
my_col = mydb['Book_Info']
email_record = my_col.find()
for i in email_record:
    # 对于每个类别的数据量进行排序
    data1.append({"商品id": i["商品id"], "标题": i['标题'],
                  "评价": i['评价'],"总评数":i['总评数']})

list2 = sorted(data1, key=operator.itemgetter('总评数'), reverse=True)
list2 = list2[:10]
# for i in list2:
#     print(i['评价'])
for i in list2:
    strlist = i['评价'].split('，')
    for j in strlist:
        if j == '':
            strlist.remove(j)
    pinglun.append(strlist)
rwords=[brand for drink in pinglun for brand in drink] #将列表扁平化
count={} #空元组
for item in rwords:
    count[item]=count.get(item,0)+1 #get 查找键 item
# 使用ggplot的绘图风格，这个类似于美化了，可以通过plt.style.available查看可选值，你会发现其它的风格真的丑。。。
plt.style.use('ggplot')

# 构造数据
values = list(count.values())
feature = list(count.keys())
for i in feature:
    print({"name": i})

print(values)
print(feature)
# 设置每个数据点的显示位置，在雷达图上用角度表示
angles = np.linspace(0, 2 * np.pi, len(values), endpoint=False)

# 拼接数据首尾，使图形中线条封闭
values = np.concatenate((values, [values[0]]))
angles = np.concatenate((angles, [angles[0]]))
feature=np.concatenate((feature,[feature[0]]))   #对labels进行封闭

# 绘图
fig = plt.figure()
# 设置为极坐标格式
ax = fig.add_subplot(111, polar=True)
# 绘制折线图
ax.plot(angles, values, 'o-', linewidth=2)
# 填充颜色
ax.fill(angles, values, alpha=0.25)

# 设置图标上的角度划分刻度，为每个数据点处添加标签
ax.set_thetagrids(angles * 180 / np.pi, feature)

# 设置雷达图的范围
ax.set_ylim(0, 10)
# 添加标题
plt.title('销量前10的好评度词雷达图')
# 添加网格线
ax.grid(True)

plt.show()