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


def page_list(params={}):
    # params是从core传递来的JsGridData对象转化的字典dict
    sql = f"""
        SELECT
            vi.*, l. language,
            vt.video_type,
            dis.district,
            st.show_type,
            c.classification
        FROM
            video_info vi
        LEFT JOIN language l ON l.id = vi.language_id
        LEFT JOIN video_type vt ON vt.id = vi.video_type_id
        LEFT JOIN district dis on dis.id = vi.district_id
        LEFT JOIN show_type st ON st.id = vi.show_type_id
        LEFT JOIN classification c ON c.id = vi.classification_id
        where vi.v_name like '%%{params['search']}%%'
        LIMIT :offset,:pageSize
        """
    data = db_handler.select(sql, params)
    return data


def count(params={}):
    # params是从core传递来的JsGridData对象转化的字典dict
    sql = f"SELECT count(id) count FROM video_info where v_name like '%%{params['search']}%%'"
    data = db_handler.select(sql, fecth="one")
    return int(data["count"])

def get_id(params={}):
    sql = "select * from video_info where id = :id"
    return db_handler.select(sql, params, fecth="one")


def update(params={}):
    sql = """
        UPDATE video_info
        SET v_code = :v_code,
        v_name = :v_name,
        director = :director,
        leading_players = :leading_players,
        language_id = :language_id,
        video_type_id = :video_type_id,
        district_id = :district_id,
        synopsis = :synopsis,
        release_time = :release_time,
        episodes = :episodes,
        v_pic = :v_pic,
        show_type_id = :show_type_id,
        classification_id = :classification_id
        WHERE id = :id
        """
    db_handler.execute(sql, params)


def all():
    sql = "select * from video_info"
    return db_handler.select(sql)


def del_id(params={}):
    sql = "DELETE FROM video_info WHERE id = :id"
    db_handler.execute(sql, params)