from apps.models import mydb
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
import jieba

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
pinglun = []
my_col = mydb['comment']
stopwords = [line.strip() for line in open("百度停用词列表1.txt", 'r', encoding='utf-8').readlines()]
stopwords.append('京东')
positive = [line.strip() for line in open("NTUSD_positive_simplified1.txt", 'r', encoding='utf-8').readlines()]
# positive.append(没事')
# positive.append('没得说')
negative = [line.strip() for line in open("NTUSD_negative_simplified1.txt", 'r', encoding='utf-8').readlines()]
# email_record = my_col.find_one({"title": "唐诗三百首（儿童注音美绘本） [7-10岁]"})["details"]
for all_coment in my_col.find():
    data1 = []
    email_record = all_coment['details']
    for i in email_record:
        # 对于每个类别的数据量进行排序
        data1.append(i["all_comment"])
    # 获取初步的分词结果
    print(len(data1))
    # for i in data1[0:10]:
    #     print(i)
    jiebaword = []
    # 去停用词

    all_positive = []
    all_negative = []
    jiji = 0
    xiaoji = 0
    for line in data1:
        data2 = []
        line = line.strip('\n')
        # 清除多余的空格
        line = "".join(line.split())
        # 默认精确模式
        seg_list = jieba.cut(line, cut_all=False)
        word = "/".join(seg_list)
        # 去停用词
        for words in word:
            words = words.split('/')
            for word1 in words:
                if word1 not in stopwords:
                    data2.append(word1)
        # jiebaword.append(word)
        for words in data2:
            words = words.split('/')
            for word in words:
                if word in positive:
                    all_positive.append(word)
                elif word in negative:
                    all_negative.append(word)
        if len(all_positive) >= len(all_negative):
            jiji = jiji + 1
        else:
            xiaoji = xiaoji + 1

    # count={} #空元组
    # print(data2)
    # print(len(data2))
    # for item in data2:
    #     count[item]=count.get(item,0)+1 #get 查找键 item
    # print(len(list(count.values())))
    # print(count)
    # new_count = sorted(count.items(), key=lambda item:item[1])
    print({"负面评价": xiaoji, "正面评价": jiji})
    print({"比例": jiji / (xiaoji + jiji)})


