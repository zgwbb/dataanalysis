import requests ,json
from bs4 import  BeautifulSoup
import time
from fake_useragent import UserAgent
import xlwt
import random
# 3 评论比较难抓（json文件形式），写一个处理方法
user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
            'Opera/8.0 (Windows NT 5.1; U; en)',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ']
def get_comment(page):
    comment_list=[]
    comment_list2=[]
    user_agent = random.choice(user_agents)
    headers = {'cookie': 'shshshfpaJsAhpiXZzNtbFCHZXchb60B240F81702FF',
               "User-Agent":  user_agent,  "Referer": "https://item.jd.com/11977252.html"}
    print(headers)
    # 构造商品地址
    url_jd = 'https://sclub.jd.com/comment/productPageComments.action?callback'
    # 网页信息
    vari_p = {
        # 商品ID
        'productId': 11977252,  # 换成你想爬取的ID就可以了
        'score': 0,
        'sortType': 5,
        # 爬取页面
        'page': page,
        'pageSize': 10,
    }
    # url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=11977252&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'.format(page)
    html=requests.get(url=url_jd, params=vari_p, headers=headers)
    print(html.text)
    fileOb = open('jd.txt', 'w', encoding='utf-8')  # 打开一个文件，没有就新建一个
    fileOb.write(html.text[20:-2])
    fileOb.close()
    with open('jd.txt', 'r',encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
    # 爬取评论数的信息页面
    html_num= load_dict['productCommentSummary']

    # 爬取评论具体内容的信息页面，下边的html_comment是取出了一个列表
    html_comment= load_dict['comments']
    for each in html_comment:
        #each是一个字典，字典中包括评论者id，评论内容
        userId=each['id']
        comment_time=each['creationTime']
        comment_content=each['content']
        #append到空的备用列表中去
        comment_list.append(userId)
        comment_list.append(comment_time)
        comment_list.append(comment_content)

    # print(comment_list)
    #把每个用户评论的ID，时间，内容放一个字典里
    total_num = len(comment_list)
    user_num = total_num // 3
    for i in range(0,user_num):
        comment_dict = {}
        comment_dict['用户ID']=comment_list[(i*3)]
        comment_dict['评论时间']=comment_list[(i*3+1)]
        comment_dict['评论内容'] = comment_list[(i*3+2)]
        comment_list2.append(comment_dict)
    return comment_list2


print(get_comment(1))
# book = xlwt.Workbook()
# # 创建表单
# sheet = book.add_sheet(u'sheet1', cell_overwrite_ok=True)
#
# sheet.write(0, 0, '用户ID')
# sheet.write(0, 1, '评论时间')
# sheet.write(0, 2, '评论内容')
#
#
#
# i = 1
# for j in range(0,100):
#     time.sleep(5)
#     print(get_comment(j))
#     for k in  range(0,10):
#         id = get_comment(j)[k]['用户ID']
#         time1 = get_comment(j)[k]['评论时间']
#         conment = get_comment(j)[k]['评论内容']
#         sheet.write(i, 0, id)
#         sheet.write(i, 1, time1)
#         sheet.write(i, 2, conment)
#         print(i)
#         i = i + 1
# book.save('唐诗三百首.xls')

