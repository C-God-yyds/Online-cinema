# -*- coding: utf-8 -*-
# author lby
from db import db_handler


def add(params={}):
    sqls = []
    video_info_sql = """
        INSERT INTO video_info (
            v_code,
            v_name,
            director,
            leading_players,
            language_id,
            video_type_id,
            district_id,
            synopsis,
            episodes,
            release_time,
            show_type_id,
            v_pic,
            classification_id
        )
        VALUES
        (
            :v_code,
            :v_name,
            :director,
            :leading_players,
            :language_id,
            :video_type_id,
            :district_id,
            :synopsis,
            :episodes,
            :release_time,
            :show_type_id,
            :v_pic,
            :classification_id
        )
        """
    sqls.append({
        "sql": video_info_sql,
        "params": params
    })

    video_labels_sql = "insert into video_labels (v_code,label_id) values (:v_code,:label_id)"

    label_ids = params["label_ids"].split(",")
    for label_id in label_ids:
        sqls.append({
            "sql": video_labels_sql,
            "params": {"v_code": params["v_code"], "label_id": label_id}
        })

    db_handler.execute_many(sqls)