# -*- coding: utf-8 -*-
# author lby
from db import db_handler


def last_episode_num(params={}):
    sql = "SELECT episode_num FROM video_lib WHERE v_code = :v_code ORDER BY episode_num DESC LIMIT 1"
    return db_handler.select(sql, params, fecth="one")


def add(params={}):
    sql = """
        INSERT INTO video_lib (
            v_code,
            v_name,
            episode_num,
            path,
            upload_time
        )
        VALUES
        (
            :v_code,
            :v_name,
            :episode_num,
            :path,
            CURRENT_TIMESTAMP()
        )
        """

    sqls = []
    for file in params["files"]:
        file["v_code"] = params["v_code"]
        file["v_name"] = params["v_name"]
        sqls.append({
            "sql": sql,
            "params": file
        })

    db_handler.execute_many(sqls)