# -*- coding: utf-8 -*-
# author lby
import os

from flask import Blueprint, request

from core import video_core

video = Blueprint("video", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__)).replace("route", "")

@video.route("/add", methods=["GET", "POST"])
def add():
    # 除了上传文件指定 普通参数使用request.form
    params = dict(request.form)
    # 上传文件提前
    file = request.files.get("v_pic")

    params["files"] = []

    v_code = params["v_code"]
    v_name = params["v_name"]

    # 最后一集
    last_episode_num = video_core.last_episode_num(params)

    episode_num = int(last_episode_num.json["episode_num"])

    # 遍历上传文件的文件名集合
    for filename in request.files:
        file = request.files.get(filename)  # 根据文件名拿上传文件
        if file:
            episode_num += 1  # 集数+1
            path = os.path.join(BASE_DIR, "data", v_code + "&" + v_name + "第" + episode_num.__str__() + "集&" + file.filename)
            file.save(path)  # 保存到硬盘
            params["files"].append({
                "path": path,
                "episode_num": episode_num
            })

    res = video_core.add(params)

    print(res.json)
    return res


# 视频的列表video_lib，操作只做删除