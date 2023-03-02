# -*- coding: utf-8 -*-
# author lby
from db import db_handler


def add(params={}):
    sqls = []
    # 新增角色，新增2个表，角色表本身和菜单关联角色表，需要把新增两个表的操作放到一个事务
    # 1、新增角色的SQL
    role_sql = "insert into role (role_code,role_name) values (:role_code,:role_name)"
    sqls.append({
        "sql": role_sql,
        "params": params
    })

    # 2、新增菜单关联角色表的SQL
    role_menu_sql = "insert into role_menu (role_code,menu_code) values (:role_code,:menu_code)"

    codes = params["codes"].split(",")

    for menu_code in codes:
        role_menu_params = {
            "role_code": params["role_code"],
            "menu_code": menu_code
        }

        sqls.append({
            "sql": role_menu_sql,
            "params": role_menu_params
        })

    # 批量执行SQL，有事务
    db_handler.execute_many(sqls)


def page_list(params={}):
    # params是从core传递来的JsGridData对象转化的字典dict
    sql = f"""
        SELECT * from role
        where role_name like '%%{params['search']}%%'
        LIMIT :offset,:pageSize
        """
    menus = db_handler.select(sql, params)
    return menus


def count(params={}):
    # params是从core传递来的JsGridData对象转化的字典dict
    sql = f"SELECT count(id) count FROM role where role_name like '%%{params['search']}%%'"
    data = db_handler.select(sql, fecth="one")
    return int(data["count"])


def get_id(params={}):
    sql = "select * from role where id = :id"
    return db_handler.select(sql, params, fecth="one")


def role_menus(params={}):
    sql = "select * from role_menu where role_code = :role_code"
    return db_handler.select(sql, params)


def update(params={}):
    sqls = []
    # 1、修改角色
    role_update = "update role set role_name = :role_name where id = :id"
    sqls.append({
        "sql": role_update,
        "params": params
    })
    # 2、修改角色的菜单逻辑
    # 2-1、删除当前角色在role_menu的关联记录
    role_menu_del = "delete from role_menu where role_code = :role_code"
    sqls.append({
        "sql": role_menu_del,
        "params": params
    })
    # 2-2、新增当前角色在role_menu的关联记录
    role_menu_sql = "insert into role_menu (role_code,menu_code) values (:role_code,:menu_code)"

    codes = params["codes"].split(",")

    for menu_code in codes:
        role_menu_params = {
            "role_code": params["role_code"],
            "menu_code": menu_code
        }

        sqls.append({
            "sql": role_menu_sql,
            "params": role_menu_params
        })

    db_handler.execute_many(sqls)


def del_id(params={}):
    sqls = []
    # 1、删除role_menu
    role_menu_sql = "DELETE FROM role_menu WHERE role_code = (SELECT role_code FROM role WHERE id = :id)"
    sqls.append({
        "sql": role_menu_sql,
        "params": params
    })

    # 2、删除role
    role_sql = "DELETE FROM role WHERE id = :id"
    sqls.append({
        "sql": role_sql,
        "params": params
    })

    db_handler.execute_many(sqls)


def all():
    sql = "select * from role"
    return db_handler.select(sql)