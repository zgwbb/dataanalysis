import requests ,json
from bs4 import  BeautifulSoup
import time
from fake_useragent import UserAgent
import csv
import random



def main(start):
    """
    开始爬取
    :return:
    """
    # 第一步解析网页
    comments_jd = begain_scraping(start)
    # 第二步 爬取评论并保存文件
    python_comments(comments_jd)

def begain_scraping(page):
    # 3 评论比较难抓（json文件形式），写一个处理方法
    user_agents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
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
    comment_list=[]
    comment_list2=[]
    user_agent = random.choice(user_agents)
    Cookie = "__jdu=1939036532; shshshfpa=c2ca7bf1-a75d-7c99-fe4d-929664e2e628-1599807572; shshshfpb=pMoVs%20skg372fiiAXfhN9Kw%3D%3D; cn=0; __jdv=122270672|direct|-|none|-|1614044189961; pinId=U1k4pyyGNm92LuDJZbo9dbV9-x-f3wj7; pin=jd_6c7630206fc6a; unick=jd_131894rzm; _tp=BThnONp5h%2FrMsyLEE88kZa9mT2H7fPij%2F1dasayXyq4%3D; _pst=jd_6c7630206fc6a; user-key=79730242-2c4e-467f-9e3a-cc17b918a919; _gcl_au=1.1.2029733887.1614266045; shshshfp=0289894c2e1b6ebe45d9ec0f03d7d15e; TrackID=19u5ZbWau4agPawv6UA0UnRVhWIi93IgyNWH_VpQBlm0K0YHiGwFnLRIeLTipiVxMYadD5Mr-__AmjUNRbQfiCkBSsOOaTCEes_E8vTIrjls; jwotest_product=99; areaId=19; ipLoc-djd=19-1677-19377-0; __jdc=122270672; __jda=122270672.1939036532.1591949927.1615288648.1615290947.40; JSESSIONID=DA48FBA9096671FBD185BFCE7149DC00.s1; shshshsID=2a051844a5ac3e529aac7b20f13e18c7_2_1615292674536; __jdb=122270672.2.1939036532|40.1615290947; 3AB9D23F7A4B3C9B=KGCBCIF6XSW5NJIEI2QWSOLVSFZNPVN6J2GKAGPZP34J63YXUFCJUV5FILUQYQTYGPNGASUGIOHXYVVD5TN7ATZXPA"
    headers = {"Cookie":Cookie,  "User-Agent":  user_agent,  "Referer": "https://item.jd.com/11487454.html"}
    # 构造商品地址
    url_jd = 'https://sclub.jd.com/comment/productPageComments.action?callback'
    # 网页信息
    vari_p = {
        # 商品ID
        'productId': 11487454,  # 换成你想爬取的ID就可以了
        'score': 0,
        'sortType': 5,
        # 爬取页面
        'page': page,
        'pageSize': 10,
    }
    comment_jd =requests.get(url=url_jd, params=vari_p, headers=headers)
    return  comment_jd


def python_comments(comment_resp):
    #爬取数据并且写入评论
    comment_list = []
    comment_js = comment_resp.text

    comment_dict = json.loads(comment_js)
    comments_jd = comment_dict['comments']
    for each in comments_jd:
        #each是一个字典，字典中包括评论者id，评论内容
        userId=each['id']
        comment_time=each['creationTime']
        comment_content=each['content']
        #append到空的备用列表中去
        comment_list.append(userId)
        comment_list.append(comment_time)
        comment_list.append(comment_content)
    # for comment in comments_jd:
    #     user = comment['nickname']
    #     color = comment['productColor']
    #     comment_python = comment['content']
    print(comment_list)
    total_num = len(comment_list)
    user_num = total_num // 3
    for i in range(0, user_num):
        comment_dict = {}
        comment_dict['用户ID'] = comment_list[(i * 3)]
        comment_dict['评论时间'] = comment_list[(i * 3 + 1)]
        comment_dict['评论内容'] = comment_list[(i * 3 + 2)]
        # 写入文件
        time.sleep(1)
        with open('中国古代寓言故事（中小学课外阅读 无障碍阅读）快乐读书吧三年级下册阅读 智慧熊图书.csv', 'a', newline='')as csv_file:
            rows = (comment_dict['用户ID'], comment_dict['评论时间'], comment_dict['评论内容'])
            writer = csv.writer(csv_file)
            writer.writerow(rows)

if __name__ == '__main__':
    # 循环100次
    ran_num = random.sample(range(0, 100), 100)
    for page in ran_num:
        print(page)
        time.sleep(2)
        main(start=page)
