# -*- coding: utf-8 -*-
# author lby
from exts import db

"""
查询（单条或多条）数据
dict的方式返回数据
:param sql: SQL字符串，select * from xxx where name=:name
:param params: dict类型，{'name':'zhangsan'}
:param fecth: 字符串"all"或者"one"，默认"all"返回全部数据，返回格式为[{},{}],如果fecth='one',返回单条数据，格式为dict
"""
def select(sql, params={}, fecth='all'):
    resultProxy = db.session.execute(sql, params)
    if fecth == 'one':
        result_tuple = resultProxy.fetchone()
        if result_tuple:
            '''
            resultProxy.keys()，查询的字段
            list(result_tuple)，查询的字段对应的字段值
            zip(resultProxy.keys(), result_tuple)，拉链，每个元素都是(字段名,值)这样的对偶元组
            dict(zip(resultProxy.keys(), result_tuple))，每个对偶元组转为dict的一组kv对
            '''
            result = dict(zip(resultProxy.keys(), result_tuple))
        else:
            return None
    else:
        result_tuple_list = resultProxy.fetchall()
        if result_tuple_list:
            result = []
            keys = resultProxy.keys()
            for row in result_tuple_list:
                result_row = dict(zip(keys, row))
                result.append(result_row)
        else:
            return None
    return result


"""
分页查询
:param sql: select * from xxx where name=:name
:param params:{'name':'zhangsan'}
:param page: 1，整数类型，查询第几页
:param page_size: 整数类型，没有查询多少条
返回list
"""
def select_pagetion(sql, params={}, page=1, page_size=15):
    sql_count = """select count(*) as count from (%s) _count""" % sql
    total_count = get_count(sql_count, params)
    sql_page = '%s limit %s,%s' % (sql, (page - 1) * page_size, page_size)
    print('sql_page:', sql_page)
    result = select(sql_page, params, 'all')
    result_dict = {'results': result, 'count': total_count}
    return result_dict


"""
增删改
:param sql: select * from xxx where name=:name
:param params:{'name':'zhangsan'}
"""
def execute(sql, params={}):
    print('sql', sql)
    db.session.execute(sql, params)
    db.session.commit()


"""
查询count
"""
def get_count(sql, params={}):
    return int(select(sql, params, fecth='one').get('count'))


"""
执行多条SQL，带事务回滚
参数sqls，list或者tuple类型，集合元素类型为dict
例如
(
    {"sql": "insert into user(username) values (:username)", "params": {"username": "lisi1"}},
    {"sql": "insert into user(username) values (:username)", "params": {"username": "lisi2"}},
    {"sql": "insert into user(username) values (:username)", "params": {"username": "lisi3"}}
)
"""
def execute_many(sqls):
    print(sqls)
    if not isinstance(sqls, (list, tuple)):
        raise Exception('type of the parameters must be list or tuple')
    if len(sqls) == 0:
        raise Exception("parameters's length can't be 0")
    for statement in sqls:
        if not isinstance(statement, dict):
            raise Exception("parameters erro")
    try:
        for s in sqls:
            db.session.execute(s.get('sql'), s.get('params'))
        db.session.commit()  # 提交事务
    except Exception as e:
        db.session.rollback()  # 回滚
        raise Exception("execute sql fail ,is rollback")
