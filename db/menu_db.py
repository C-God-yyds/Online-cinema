# -*- coding: utf-8 -*-
# author lby
from db import db_handler


# 查询所有一级菜单
def first_all():
    sql = "select * from menu where menu_level = '1' order by sort"
    first_menus = db_handler.select(sql)
    return first_menus


def add(params={}):
    sql = """
        INSERT INTO menu 
        (menu_code,menu_name,menu_url,menu_level,parent_id,sort)
         VALUES 
        (:menu_code,:menu_name,:menu_url,:menu_level,:parent_id,:sort)
        """
    db_handler.execute(sql, params)


def page_list(params={}):
    # params是从core传递来的JsGridData对象转化的字典dict
    sql = f"""
        SELECT m.*, pm.menu_name parent_menu_name FROM menu m 
        LEFT JOIN menu pm ON m.parent_id = pm.id
        where m.menu_name like '%%{params['search']}%%'
        ORDER BY m.parent_id,m.sort 
        LIMIT :offset,:pageSize
        """
    menus = db_handler.select(sql, params)
    return menus


def count(params={}):
    # params是从core传递来的JsGridData对象转化的字典dict
    sql = f"SELECT count(id) count FROM menu where menu_name like '%%{params['search']}%%'"
    data = db_handler.select(sql, fecth="one")
    return int(data["count"])


def get_id(params={}):
    sql = "select * from menu where id = :id"
    return db_handler.select(sql, params, fecth="one")


def update(params={}):
    sql = """
        UPDATE menu
        SET menu_code = :menu_code,
         menu_name = :menu_name,
         menu_url = :menu_url,
         menu_level = :menu_level,
         parent_id = :parent_id,
         sort = :sort
        WHERE
            id = :id
        """
    db_handler.execute(sql, params)


def all():
    sql = "select * from menu"
    return db_handler.select(sql)


def del_id(params={}):
    sql = "DELETE FROM menu WHERE id = :id"
    db_handler.execute(sql, params)


def first_menus_username(user={}):
    sql = """
        SELECT m.* FROM menu m 
        LEFT JOIN role_menu rm ON rm.menu_code = m.menu_code
        LEFT JOIN role r ON r.role_code = rm.role_code
        LEFT JOIN admin_role ar ON ar.role_code = r.role_code 
        WHERE m.menu_level = 1 AND ar.username = :username 
        order by m.sort
        """

    return db_handler.select(sql, user)


def second_menus_username(user={}):
    sql = """
        SELECT m.* FROM menu m 
        $left_join_sql
        WHERE m.menu_level = 2 AND m.parent_id = :parent_id $other_user_sql
        order by m.sort
        """

    left_join_sql = """
        LEFT JOIN role_menu rm ON rm.menu_code = m.menu_code
        LEFT JOIN role r ON r.role_code = rm.role_code
        LEFT JOIN admin_role ar ON ar.role_code = r.role_code 
        """

    other_user_sql = "AND ar.username = :username"

    if user["username"] != "admin":
        sql = sql.replace("$left_join_sql", left_join_sql)
        sql = sql.replace("$other_user_sql", other_user_sql)
    else:
        sql = sql.replace("$left_join_sql", "")
        sql = sql.replace("$other_user_sql", "")

    return db_handler.select(sql, user)