"""
分页
这个分页的功能包括
1、根据用户请求当前页和总数据条数计算出m和n
2、根据m和n去数据中取数据
而使用property属性就可以满足需求
直接函数调用start和end就可以知道取的开始页还有结束页
"""


class Pager:
    def __init__(self, current_page):
        self.current_page = current_page
        # 规定每一页的个数
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page-1)*self.per_items
        return val

    @property
    def end(self):
        val = self.current_page*self.per_items
        return val



