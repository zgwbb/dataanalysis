from apps.models import mydb
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
import jieba

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
data1 = []
pinglun = []
my_col = mydb['comment']
# email_record = my_col.find_one({"title": "恐龙百科（儿童注音版） [7-10岁]"})["details"]
# for i in email_record:
#     # 对于每个类别的数据量进行排序
#     data1.append(i["all_comment"])
data3 = []
for all_coment in my_col.find():
    data1 = []
    email_record = all_coment['details']
    for i in email_record:
        # 对于每个类别的数据量进行排序
        data1.append(i["all_comment"])
    jiebaword = []
    for line in data1:
        line = line.strip('\n')
        # 清除多余的空格
        line = "".join(line.split())
        # 默认精确模式
        seg_list = jieba.cut(line, cut_all=False)
        word = "/".join(seg_list)
        jiebaword.append(word)
    # print(jiebaword)

    # 去停用词
    data2 = []
    stopwords = [line.strip() for line in open("百度停用词列表1.txt", 'r', encoding='utf-8').readlines()]
    stopwords.append('京东')
    positive = [line.strip() for line in open("NTUSD_positive_simplified1.txt", 'r', encoding='utf-8').readlines()]
    positive.append('没事')
    positive.append('没得说')
    negative = [line.strip() for line in open("NTUSD_negative_simplified1.txt", 'r', encoding='utf-8').readlines()]
    # stopwords.append('京东')
    # stopwords.append('快递')
    all_positive = []
    all_negative = []
    # fw = open('clean.txt', 'a+',encoding='utf-8')
    for words in jiebaword:
        words = words.split('/')
        for word in words:
            if word not in stopwords:
                data2.append(word)
                # fw.write(word + '\t')
        # fw.write('\n')
    # fw.close()
    for words in data2:
        words = words.split('/')
        for word in words:
            if word in positive:
                all_positive.append(word)
            elif word in negative:
                all_negative.append(word)
    count = {}  # 空元组
    print(data2)
    print(len(data2))
    for item in data2:
        count[item] = count.get(item, 0) + 1  # get 查找键 item
    print(len(list(count.values())))
    print(count)
    new_count = sorted(count.items(), key=lambda item: item[1])
    print({"负面词": len(all_negative), "正面词": len(all_positive)})
    print({"比例": (len(all_positive) / (len(all_negative) + len(all_positive)))*100})
    data3.append((len(all_positive) / (len(all_negative) + len(all_positive)))*100)
# for i in all_negative:
#     print(i)
print(data3)

