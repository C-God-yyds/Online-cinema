# -*- coding: utf-8 -*-
# author lby
from core.base_core import service
from db import vide_db


@service
def last_episode_num(params={}):
    data = vide_db.last_episode_num(params)
    # 从数据库查询的最后一集的集数可以不存在
    if not data:
        data = {"episode_num": 0}

    return data


@service
def add(params={}):
    vide_db.add(params)
