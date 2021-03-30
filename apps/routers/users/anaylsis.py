import pandas as pd
import random
# IO = '京东图书数据1200.xlsx'
sheet = pd.read_excel('京东图书数据1200.xlsx',engine='openpyxl')
# data=sheet.head()#默认读取前5行的数据
# data=sheet.iloc[0].values#0表示第一行 这里读取数据并不包含表头，要注意哦！
# print("读取指定行的数据：\n{0}".format(data))
# print(type(data[15]))
# 获取列数
# print(sheet.shape[1])
#  获取行数
# print(sheet.shape[0])
lange2 = []
for i in range(0, sheet.shape[0]):
    data = sheet.iloc[i].values  # 0表示第一行 这里读取数据并不包含表头，要注意哦！
    if "万" in data[16]:
        lange = data[16].split('万')
        if len(lange[0]) == 1:
            lange1 = random.randint(int(lange[0])*10000,(int(lange[0])+1)*10000)
            lange2.append(lange1)
        if len(lange[0]) == 2:
            lange1 = random.randint(int(lange[0][0:1]) * 100000, (int(lange[0][0:1]) + 1) * 100000)
            lange2.append(lange1)
        if len(lange[0]) == 3:
            lange1 = random.randint(int(lange[0][0:1]) * 1000000, (int(lange[0][0:1]) + 1) * 1000000)
            lange2.append(lange1)
    if "+" in data[16] and "万" not in data[16]:
        lange = data[16].split('+')
        if len(lange[0]) == 3:
            lange1 = random.randint(int(lange[0]), (int(lange[0]) + 100))
            lange2.append(lange1)
        if len(lange[0]) == 4:
            lange1 = random.randint(int(lange[0]), (int(lange[0]) + 1000))
            lange2.append(lange1)
    if "+" not in data[16] and "万" not in data[16]:
        lange2.append(int(data[16]))
print(len(lange2))
# fileObject = open('sampleList.csv', 'w')
# for ip in lange2:
#  fileObject.write(str(ip))
#  fileObject.write('\n')
# fileObject.close()
