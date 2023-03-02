# -*- coding: utf-8 -*-
# author lby
from functools import wraps

from flask import jsonify

from models.message_model import Message


def service(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        res = Message("200", "success")
        try:
            # 被装饰的函数，返回值是否存在
            res = fn(*args, **kwargs)
            if res is None:  # 如果返回值不存在，就给res重新改为Message()
                res = Message("200", "success")
        except Exception as e:
            res.failed()
            print(e)

        # jsonify把对象转json，如果对象中有赋值的属性，dict，int()。。。，都会报错
        try:
            res_json = jsonify(res)
        except TypeError as e:
            res_json = jsonify(res.__dict__)

        return res_json

    return wrapper