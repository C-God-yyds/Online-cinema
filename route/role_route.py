# -*- coding: utf-8 -*-
# author lby
from flask import Blueprint, request

from core import role_core

role = Blueprint("role", __name__)


@role.route("/add", methods=["GET", "POST"])
def add():
    # ajax的请求参数，request.form，是dict
    res = role_core.add(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@role.route("/list/page", methods=["GET", "POST"])
def list_page():
    res = role_core.list_page(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@role.route("/get/id", methods=["GET", "POST"])
def get_id():
    res = role_core.get_id(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@role.route("/update", methods=["GET", "POST"])
def update():
    # ajax的请求参数，request.form，是dict
    res = role_core.update(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@role.route("/del/id", methods=["GET", "POST"])
def del_id():
    # ajax的请求参数，request.form，是dict
    res = role_core.del_id(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@role.route("/all", methods=["GET", "POST"])
def all():
    # ajax的请求参数，request.form，是dict
    res = role_core.all()
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res