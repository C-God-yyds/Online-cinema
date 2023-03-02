# -*- coding: utf-8 -*-
# author lby
from flask import Blueprint, request, session

from core import menu_core

menu = Blueprint("menu", __name__)


@menu.route("/first/all", methods=["GET", "POST"])
def first_all():
    res = menu_core.first_all()
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@menu.route("/add", methods=["GET", "POST"])
def add():
    # ajax的请求参数，request.form，是dict
    res = menu_core.add(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@menu.route("/list/page", methods=["GET", "POST"])
def list_page():
    res = menu_core.list_page(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@menu.route("/get/id", methods=["GET", "POST"])
def get_id():
    res = menu_core.get_id(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@menu.route("/update", methods=["GET", "POST"])
def update():
    # ajax的请求参数，request.form，是dict
    res = menu_core.update(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@menu.route("/all", methods=["GET", "POST"])
def all():
    res = menu_core.all()
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@menu.route("/del/id", methods=["GET", "POST"])
def del_id():
    # ajax的请求参数，request.form，是dict
    res = menu_core.del_id(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@menu.route("/left", methods=["GET", "POST"])
def left():
    # 从session中获取登录的用户
    user = session["current_user"]
    # ajax的请求参数，request.form，是dict
    res = menu_core.left(user)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res