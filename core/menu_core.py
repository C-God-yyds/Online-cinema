# -*- coding: utf-8 -*-
# author lby
from flask import jsonify

from core.base_core import service
from db import menu_db
from models.js_grid_data import JsGridData
from models.message_model import Message


def first_all():
    first_menus = menu_db.first_all()
    return jsonify(first_menus)  # 把返回的[{},{}]类型的数据转换为json


# def add(params={}):
#     res = Message()
#     try:
#         # menu_db.add没有返回值，判断它有没有异常
#         menu_db.add(params)
#         res.success()
#     except:
#         res.failed()  # 有异常，给999，表示新增失败
#
#     # jsonify把对象转json，如果对象中有赋值的属性，dict，int()。。。，都会报错
#     return jsonify(res.__dict__)  # res转json

@service
def add(params={}):
    menu_db.add(params)


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
    data = menu_db.page_list(grid_data.__dict__)  # 分页数据集合

    # 2、数据的总条数
    itemsCount = menu_db.count(grid_data.__dict__)

    grid_data.data = data
    grid_data.itemsCount = itemsCount

    return jsonify(grid_data.__dict__)


@service
def get_id(params={}):
    return menu_db.get_id(params)


@service
def update(params={}):
    menu_db.update(params)


@service
def all():
    return menu_db.all()


@service
def del_id(params={}):
    # 删除角色，也删除角色菜单关联，总共要处理2个操作数据库的逻辑，使用事务
    menu_db.del_id(params)

@service
def left(user={}):
    """
    查询菜单的逻辑，需要分两次查询
    1、查询一级菜单
    2、遍历查询到一级菜单集合，根据一级的菜单的id做二级菜单父id，查询二级菜单的集合
    :param user:
    :return:
    """
    first_menus = []

    left_menus = []

    # 判断当前的登录用户，2种，普通用户和超级管理员（admin）
    if user["username"] == "admin":
        first_menus = menu_db.first_all()
    else:
        first_menus = menu_db.first_menus_username(user)

    # 遍历一级菜单，构建对应的二级菜单
    for first_menu in first_menus:
        user["parent_id"] = first_menu["id"]
        second_menus = menu_db.second_menus_username(user)
        left_menus.append({
            "first_menu": first_menu,
            "second_menus": second_menus
        })

    data = {
        "code": "200",
        "left_menus": left_menus
    }

    return data