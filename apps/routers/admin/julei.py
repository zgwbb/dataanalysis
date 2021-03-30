from apps.models import mydb
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
import jieba
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import nltk
from collections import Counter


# mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
# data1 = []
# pinglun = []
# my_col = mydb['comment']
# email_record = []
# for details in my_col.find():
#     email_record.append(details["details"])
# for i in email_record:
#     for comment1 in i:
#         data1.append(comment1["all_comment"])
# # 获取初步的分词结果
# jiebaword = []
# for line in data1:
#     line = line.strip('\n')
#     # 清除多余的空格
#     line = "".join(line.split())
#     # 默认精确模式
#     seg_list = jieba.cut(line, cut_all=False)
#     word = "/".join(seg_list)
#     jiebaword.append(word)
# # print(jiebaword)
# print("结巴分词成功")
# # 去停用词
# data2 = []
# stopwords = [line.strip() for line in open("百度停用词列表1.txt", 'r', encoding='utf-8').readlines()]
# stopwords.append('京东')
# # positive = [line.strip() for line in open("NTUSD_positive_simplified1.txt", 'r', encoding='utf-8').readlines()]
# # positive.append('没事')
# # positive.append('没得说')
# # negative = [line.strip() for line in open("NTUSD_negative_simplified1.txt", 'r', encoding='utf-8').readlines()]
# # stopwords.append('京东')
# # stopwords.append('快递')
# all_positive = []
# all_negative = []
# fw = open('clean.txt', 'a+',encoding='utf-8')
# for words in  jiebaword:
#     words = words.split('/')
#     for word in words:
#         if word not in stopwords:
#             data2.append(word)
#             fw.write(word + '\t')
#     fw.write('\n')
# fw.close()
print("去停用词成功")
with open('clean.txt', "r", encoding='utf-8') as fr:
    wordList = fr.readlines()
# 生成tfidf矩阵
transformer=TfidfVectorizer()
tfidf = transformer.fit_transform(wordList)
# 转为数组形式
tfidf_arr = tfidf.toarray()

print(tfidf_arr.shape)
print(tfidf_arr)
#
# 分成3类.使用余弦相似分析
km = nltk.cluster.kmeans.KMeansClusterer(num_means=3, distance=nltk.cluster.util.cosine_distance)
km.cluster(tfidf_arr)

for data,word in zip(tfidf_arr,wordList):
    print(km.classify(data),word)
# print("分类成功")
# index=np.empty([55001,2], dtype = int)
# i=0
# for data in tfidf_arr:
#     index[i][0] = km.classify(data)
#     index[i][1]=km.classify(data)
#     i+=1
# # 获取分类文档，把不同类的文本分开装在3个文件
# for ind,line in enumerate(wordList):
#     for i in range(0,55001):
#         if ind == index[i][0]:
#             fw = open('cluster' + str(index[i][1]) + '.txt', 'a+', encoding='utf-8')
#             fw.write(line)
#
# # 得到分类文档之后，再分别统计不同类之中出现频率较高的词，从中选择为主题词。
# for i in range(0,3):
#     with open('cluster' + str(i) + '.txt', "r", encoding='utf-8') as fr:
#         lines = fr.readlines()
#
#     all_words = []
#     for line in lines:
#         line = line.strip('\n')
#         line = line.split('\t')
#         for word in line:
#             all_words.append(word)
#     c = Counter()
#     for x in all_words:
#         if len(x) > 1 and x != '\r\n':
#             c[x] += 1
#
#     print('主题' + str(i+1) + ' 词频统计结果：')
#     # 输出词频最高的10个词
#     for (k, v) in c.most_common(10):
#         print(k,':',v)
# print("成功得到结果")
