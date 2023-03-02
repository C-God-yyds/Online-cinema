# -*- coding: utf-8 -*-
# author lby
from core.base_core import service
from db import role_db
from models.js_grid_data import JsGridData


@service
def add(params={}):
    role_db.add(params)


@service
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
    data = role_db.page_list(grid_data.__dict__)  # 分页数据集合

    # 2、数据的总条数
    itemsCount = role_db.count(grid_data.__dict__)

    grid_data.data = data
    grid_data.itemsCount = itemsCount

    return grid_data


@service
def get_id(params={}):
    # 1、根据id查询role
    role = role_db.get_id(params)

    # 2、根据role_code查询role_menu
    role_menus = role_db.role_menus(role)

    data = {
        "role": role,
        "role_menus": role_menus
    }

    return data


@service
def update(params={}):
    # 修改角色，也修改角色的菜单，认为是一定修改角色的菜单，总共要处理3个操作数据库的逻辑，使用事务
    role_db.update(params)

@service
def del_id(params={}):
    # 删除角色，也删除角色菜单关联，总共要处理2个操作数据库的逻辑，使用事务
    role_db.del_id(params)


@service
def all():
    return role_db.all()