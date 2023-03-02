# -*- coding: utf-8 -*-
# author lby
from flask import Blueprint, send_from_directory, request, session, jsonify, render_template

from core import admin_core

admin = Blueprint("user", __name__)

@admin.route("/login.html")
def login_html():
    return send_from_directory("static","pages/login.html")


@admin.route("/index.html")
def index_html():
    # 权限校验，在路由跳转index页时，判断session中有没有用户，没有就没有登录，没登录跳转登录页
    # try:
    #     user = session["current_user"]
    # except KeyError as e:  # 根据current_user获取user有异常KeyError
    #     return send_from_directory("static", "pages/login.html")

    return send_from_directory("static","pages/index.html")


@admin.route("/index.html")
def login_name():
    res = admin_core.login(request.form)
    return jsonify(res.__dict__)


# 登录
@admin.route("/login", methods=["GET", "POST"])
def login():
    print(request.form["username"] + ", " + request.form["password"])

    res = admin_core.login(request.form)

    # 登录成功，保存用到session
    if res.code == "200":
        session["current_user"] = res.data

    return jsonify(res.__dict__)





@admin.route("/add", methods=["GET", "POST"])
def add():
    # ajax的请求参数，request.form，是dict
    res = admin_core.add(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@admin.route("/load/select", methods=["GET", "POST"])
def load_select():
    # ajax的请求参数，request.form，是dict
    res = admin_core.load_select(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res

@admin.route("/get/id", methods=["GET", "POST"])
def get_id():
    res = admin_core.get_id(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res

@admin.route("/list/page", methods=["GET", "POST"])
def list_page():
    res = admin_core.list_page(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res

@admin.route("/update", methods=["GET", "POST"])
def update():
    # ajax的请求参数，request.form，是dict
    res = admin_core.update(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res

@admin.route("/del/id", methods=["GET", "POST"])
def del_id():
    # ajax的请求参数，request.form，是dict
    res = admin_core.del_id(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res

@admin.route("/all", methods=["GET", "POST"])
def all():
    # ajax的请求参数，request.form，是dict
    res = admin_core.all()
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res
