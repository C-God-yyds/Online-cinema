# -*- coding: utf-8 -*-
# author lby
class JsGridData:
    pageIndex = 0  # 第几页
    pageSize = 0  # 每页几条数据，作为limit查询的步长参数
    """
    pageIndex=1, pageSize=3, offset=0=(1-1)*3=0
    pageIndex=2, pageSize=3, offset=3=(2-1)*3=3
    pageIndex=3, pageSize=3, offset=6=(3-1)*3=6
    
    offset=(pageIndex-1)*pageSize
    """
    offset = 0  # 偏移量，limit查询的偏移量参数，查询到起始位置，从0开始

    data = []  # 返回给前端的查询数据
    itemsCount = 0  # 总条数
    search = ""  # 查询条件

    def __init__(self, params={}):
        self.pageIndex = int(params["pageIndex"])
        self.pageSize = int(params["pageSize"])
        self.offset = (self.pageIndex - 1) * self.pageSize
        self.search = params["search"]

