# -*- coding: utf-8 -*-
# author lby
from db import db_handler


# 登录
def login(params={}):
    # 登录查询，因为登录成功之后要把登录的用户保存session中，所以根据用户名和密码查询完整的用户的数据
    sql = "select * from admin where username = :username and password = :password"
    user = db_handler.select(sql, params, fecth="one")
    return user


def add(params={}):
    sqls = []
    # 新增用户，新增2个表，用户表本身和用户关联角色表，需要把新增两个表的操作放到一个事务
    # 1、新增用户的SQL
    admin_sql = "INSERT INTO admin (username,password,real_name,job_no) VALUES (:username,:password,:real_name,:job_no)"
    sqls.append({
        "sql": admin_sql,
        "params": params
    })

    # 2、新增用户关联角色表的SQL
    admin_role_sql = "INSERT INTO admin_role (username,role_code) VALUES (:username,:role_code)"
    sqls.append({
        "sql": admin_role_sql,
        "params": params
    })

    # 批量执行SQL，有事务
    db_handler.execute_many(sqls)


def load_select(params={}):
    sql = f"select * from {params['tab_name']}"
    return db_handler.select(sql)

def get_id(params={}):
    sql = "select * from admin where id = :id"
    return db_handler.select(sql, params, fecth="one")


def page_list(params={}):
    # params是从core传递来的JsGridData对象转化的字典dict
    sql = f"""
        SELECT * from admin
        where username like '%%{params['search']}%%'
        LIMIT :offset,:pageSize
        """
    menus = db_handler.select(sql, params)
    return menus


def count(params={}):
    # params是从core传递来的JsGridData对象转化的字典dict
    sql = f"SELECT count(id) count FROM admin where username like '%%{params['search']}%%'"
    data = db_handler.select(sql, fecth="one")
    return int(data["count"])


def admin_roles(params={}):
    sql = "select * from admin_role where username = :username"
    return db_handler.select(sql, params)


def update(params={}):
    sqls = []
    # 1、修改用户
    admin_update = """update admin 
                    set username = :username,
                    password = :password,
                    real_name = :real_name,
                    job_no = :job_no
                    where id = :id"""
    sqls.append({
        "sql": admin_update,
        "params": params
    })
    # 2、修改用户的菜单逻辑
    # 2-1、删除当前用户在admin_role的关联记录
    admin_role_del = "delete from admin_role where username = :username"
    sqls.append({
        "sql": admin_role_del,
        "params": params
    })
    # 2-2、新增当前角色在admin_role的关联记录
    admin_role_sql = "insert into admin_role (username,role_code) values (:username,:role_code)"

    codes = params["codes"].split(",")

    for role_code in codes:
        admin_role_params = {
            "username": params["username"],
            "role_code": role_code
        }

        sqls.append({
            "sql": admin_role_sql,
            "params": admin_role_params
        })

    db_handler.execute_many(sqls)


def del_id(params={}):
    sqls = []
    # 1、删除admin_role
    admin_role_sql = "DELETE FROM admin_role WHERE username = (SELECT username FROM admin WHERE id = :id)"
    sqls.append({
        "sql": admin_role_sql,
        "params": params
    })

    # 2、删除user
    admin_sql = "DELETE FROM admin WHERE id = :id"
    sqls.append({
        "sql": admin_sql,
        "params": params
    })

    db_handler.execute_many(sqls)

def all():
    sql = "select * from admin"
    return db_handler.select(sql)