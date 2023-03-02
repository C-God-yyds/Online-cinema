# -*- coding: utf-8 -*-
# author lby
from flask import jsonify

from core.base_core import service
from db import admin_db
from models.js_grid_data import JsGridData
from models.message_model import Message


# 登录
def login(params={}):
    user = admin_db.login(params)
    res = Message("999", "failed")
    # 判断user是否存在，如果存在就是登录成功，需要返回user
    if user:
        res.success()
        res.data = user

    return res


@service
def add(params={}):
    admin_db.add(params)


# 列表、修改、删除


@service
def load_select(params={}):
    return admin_db.load_select(params)


@service
def get_id(params={}):
    return admin_db.get_id(params)

def list_page(params={}):
    # 把route传递来的request.form给JsGridData
    grid_data = JsGridData(params)

    """
    JSGrid的与后台的返回数据格式有要求，json对象
    {
        "data": 查询的数据集合,  # 表格展示数据
        "itemsCount": 你的数据的总条数   #  计算页码
    }
    """

    # 1、查询的数据集合
    data = admin_db.page_list(grid_data.__dict__)  # 分页数据集合

    # 2、数据的总条数
    itemsCount = admin_db.count(grid_data.__dict__)

    grid_data.data = data
    grid_data.itemsCount = itemsCount

    return jsonify(grid_data.__dict__)


@service
def update(params={}):
    # 修改角色，也修改角色的菜单，认为是一定修改角色的菜单，总共要处理3个操作数据库的逻辑，使用事务
    admin_db.update(params)

@service
def del_id(params={}):
    # 删除角色，也删除角色菜单关联，总共要处理2个操作数据库的逻辑，使用事务
    admin_db.del_id(params)


@service
def all():
    return admin_db.all()