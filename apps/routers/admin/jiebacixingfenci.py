from apps.models import mydb
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
import jieba
import jieba.posseg as ps
import jieba.analyse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import nltk
from collections import Counter

# mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
# data1 = []
# pinglun = []
# my_col = mydb['comment']
# email_record1 = my_col.find()
# email_record = []
# for i in email_record1:
#     email_record.append(i["details"])
# # email_record = my_col.find_one({"title": "恐龙百科（儿童注音版） [7-10岁]"})["details"]
# for i in email_record:
#     for details in i:
#         data1.append(details["all_comment"])
# # 获取初步的分词结果
# jiebaword = []
# for line in data1:
#     line = line.strip('\n')
#     # 清除多余的空格
#     line = "".join(line.split())
#     # 默认精确模式
#     # seg_list = jieba.cut(line, cut_all=False)
#     # word = "/".join(seg_list)
#     word = ps.lcut(line)
#     jiebaword.append(word)
# # print(jiebaword)
#
# # 去停用词
# data2 = []
# stopwords = [line.strip() for line in open("百度停用词列表1.txt", 'r', encoding='utf-8').readlines()]
# stopwords.append('京东')
# positive = [line.strip() for line in open("NTUSD_positive_simplified1.txt", 'r', encoding='utf-8').readlines()]
# positive.append('没事')
# positive.append('没得说')
# negative = [line.strip() for line in open("NTUSD_negative_simplified1.txt", 'r', encoding='utf-8').readlines()]
# # stopwords.append('京东')
# stopwords.append('快递')
# all_positive = []
# all_negative = []
# # fw = open('clean.txt', 'a+',encoding='utf-8')
# for words in  jiebaword:
#     # words = words.split('/')
#     for word in words:
#         # print(word)
#         if list(word)[0] not in stopwords:
#             data2.append(word)
#     #         fw.write(word + '\t')
#     # fw.write('\n')
# # fw.close()
# # print("ok")
# print(data2)
# 读取文件
# fw = open('clean.txt', 'a+',encoding='utf-8')
# for words in  jiebaword:
#     words = words.split('/')
#     for word in words:
#         if word not in stopwords:
#             data2.append(word)
#             fw.write(word + '\t')
#     fw.write('\n')
# fw.close()
# print("ok")
# fw = open('形容词.txt', 'a+',encoding='utf-8')
# num = 0
# for i in data2:
#     if list(i)[1] == 'a':
#         fw.write(list(i)[0]+'\t')
#     else:
#         continue
#     num = num+1
#     if num/10 ==0:
#         fw.write('\n')
# fw.close()

file=open('形容词.txt',encoding='utf-8')
str=file.read()
qiege = str.split('\t')
count={} #空元组
for item in qiege:
    count[item]=count.get(item,0)+1 #get 查找键 item
print(count)

rs= jieba.analyse.textrank(str,allowPOS=('a'))
print({"textrank结果": rs})
print('返回关键词及权重值')
rs=jieba.analyse.textrank(str,20,True,('a',))
# print(rs)
# print(type(rs))
for k,v in rs:
    print(k,v,sep="\t")




