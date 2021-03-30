stopwords = [line.strip() for line in open("百度停用词列表1.txt", 'r', encoding='utf-8').readlines()]
print(stopwords)