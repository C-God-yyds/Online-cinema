# -*- coding: utf-8 -*-
# author lby
class Message:
    code = ""
    msg = ""
    data = {}

    def __init__(self, code="", msg=""):
        self.code = code
        self.msg = msg

    # 标准是设置code="200", msg="success"，单允许自己重新设置成功的code和msg
    def success(self, code="200", msg="success"):
        self.code = code
        self.msg = msg

    def failed(self, code="999", msg="failed"):
        self.code = code
        self.msg = msg