from apps.models import mydb
from functools import reduce

my_col = mydb['comment']
my_data = mydb['Book_Info']
url = ["https://item.jd.com/11977252.html",
"https://item.jd.com/11905669.html",
"https://item.jd.com/11977270.html",
"https://item.jd.com/11977266.html",
"https://item.jd.com/12715197.html",
"https://item.jd.com/12638691.html",
"https://item.jd.com/12401321.html",
"https://item.jd.com/11051349.html",
"https://item.jd.com/11179524.html",
"https://item.jd.com/11487454.html"]

data1 = []
data2 = []
data3 = []
num = 0
for all_coment in my_col.find():
    email_record = my_data.find_one({"标题":all_coment['title']})
    data1.append({"商品id": email_record["商品id"],"好评率":email_record["好评率"],"作者":email_record["作者"],"标题": email_record['标题'],
                    "销量": email_record['总评数'], "类型":email_record[ "类型"],"价格":email_record["价格"],
                  "折扣":email_record["折扣"],"出版社":email_record["出版社"]})
    data2.append(email_record['标题'])
    data3.append(email_record["好评率"])
# 去重
run_function = lambda x, y: x if y in x else x + [y]
data1= reduce(run_function, [[], ] + data1)
for i in data1:
    i['url'] = url[num]
    print(i)
    num+=1
print(data1)