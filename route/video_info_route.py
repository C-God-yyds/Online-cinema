# -*- coding: utf-8 -*-
# author lby
import os

from flask import Blueprint, request

from core import video_info_core

video_info = Blueprint("video_info", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__)).replace("route", "")


@video_info.route("/add", methods=["GET", "POST"])
def add():
    # 除了上传文件指定 普通参数使用request.form
    params = dict(request.form)
    # 上传文件提前
    file = request.files.get("v_pic")

    params["file"] = file
    params["BASE_DIR"] = BASE_DIR

    res = video_info_core.add(params)

    print(res.json)
    return res


@video_info.route("/list/page", methods=["GET", "POST"])
def list_page():
    res = video_info_core.list_page(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@video_info.route("/get/id", methods=["GET", "POST"])
def get_id():
    res = video_info_core.get_id(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@video_info.route("/update", methods=["GET", "POST"])
def update():
    # ajax的请求参数，request.form，是dict
    res = video_info_core.update(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@video_info.route("/del/id", methods=["GET", "POST"])
def del_id():
    # ajax的请求参数，request.form，是dict
    res = video_info_core.del_id(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@video_info.route("/all", methods=["GET", "POST"])
def all():
    res = video_info_core.all()
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res
