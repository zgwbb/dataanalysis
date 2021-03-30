from apps.models import mydb
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
import operator
import pandas as pd
from functools import reduce
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
# mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

data1 = []
pinglun = []
my_col = mydb['Book_Info']
email_record = my_col.find()
for i in email_record:
    # 对于每个类别的数据量进行排序
    data1.append({"商品id": i["商品id"], "标题": i['标题'],
                  "评价": i['评价'],"总评数":i['总评数']})
run_function = lambda x, y: x if y in x else x + [y]
data1= reduce(run_function, [[], ] + data1)
list2 = sorted(data1, key=operator.itemgetter('总评数'), reverse=True)
list2 = list2[:10]
for i in list2:
    print(i)
for i in list2:
    strlist = i['评价'].split('，')
    for j in strlist:
        if j == '':
            strlist.remove(j)
    pinglun.append(strlist)
te = TransactionEncoder()
#进行 one-hot 编码
te_ary = te.fit(pinglun).transform(pinglun)
df = pd.DataFrame(te_ary, columns=te.columns_)
#利用 Apriori 找出频繁项集
freq = apriori(df, min_support=0.6, use_colnames=True)
# print(freq)
# print(freq.describe())
result = association_rules(freq, metric="confidence", min_threshold=0.6)

#筛选出提升度和置信度满足条件的关联规则
result = result[ ( result["lift"] > 1) & (result["confidence"] > 0.8) ]
das = result.to_dict(orient='records')
print(result)
print(len(das))
dataSet = []
dataRelate =[]
categories = ['品质一流', '印刷上乘', '图文清晰', '图案精美', '优美详细', '质地上乘','字体适宜', '毫无异味',
              '纸张精良', '精美雅致', '轻松有趣', '简单清晰', '增长知识', '内容精彩', '内容丰富', '色彩艳丽']
categories_gai = {}
num = 0
for i in categories:
    categories_gai[i] = num
    num = num+1
for i in das:
    print(i)
    # i['consequents'] = ",".join(list(i['consequents']))
    # i['consequents'] = i['consequents'].decode("unicode-escape")
    # i['antecedents'] = ",".join(list(i['antecedents']))
    # i['antecedents'] = i['antecedents'].decode("unicode-escape")
    # dataRelate.append(i)
    #  {source:'土豆',target:'大米',value:0.73},
    # dataSet.append({"name":item1,"category":categories_gai[list(i['antecedents'])[0]],"value":i['support']})
    # dataRelate.append({"antecedent":item1,"consequent":item2,"confidence":i['confidence']})
# for i in dataRelate:
#     print(i)

