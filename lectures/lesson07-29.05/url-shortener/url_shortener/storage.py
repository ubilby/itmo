"""
часть 2
"""

import sqlite3
import os.path as path

from url_shortener.converter import convert, inverse

SQL_UPDATE_SHORT_URL = """
                UPDATE shortener SET short_url=?
                WHERE id=?
"""

SQL_SELECT_ALL = """
    SELECT
        id, original_url, short_url, created
    FROM
        shortener
""" #переменные заданные константой - по соглашению - константа. перечисление можно заменить звездочкой. тут мы создаем SQLзапрос

SQL_SELECT_URL_BY_PK = SQL_SELECT_ALL + " WHERE id=?"

SQL_SELECT_URL_BY_ORIGIN = SQL_SELECT_ALL + " WHERE original_url=?"

SQL_INSERT_URL = """
        INSERT INTO shortener (
        original_url
    )    VALUES (
            ?
    )
"""

#вопросительный знак - неименованный параметр


def dict_factory(cursor, row): #тут нужно разобраться!!!
    d = {}
    #print("row:", row) #Сатана!!!
    #print("col:", cursor.description)
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect(db_name = None):
    
    if db_name is None:
        db_name = ":memory:"
        
    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    return conn


def initialize(conn): #возможно путь нужно будет задать иначе
    with conn:
        script_filename = path.join(path.dirname(__file__), "schema.sql")
        with open(script_filename) as f:
            conn.executescript(f.read())


def add_url(conn, url, domain = ""):
    url = url.strip("/")
    if not url:
        return #здесь должна быть ошибка

    with conn:  #зачем тут два уровня with?
        found = find_url_by_origin(conn, url)

        if found:
            return found.get("short_url")

        cursor = conn.execute(SQL_INSERT_URL, (url,))
        pk = cursor.lastrowid #после выполнениея одного инсерта у курсора есть инфа о Примари кей последней записи
        short_url = "{}/{}".format(domain.strip("/"), convert(pk,))
        conn.execute(SQL_UPDATE_SHORT_URL, (short_url, pk))
        
        #здесь магия
        return short_url

def find_all(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()


def find_url_by_pk(conn, pk):
    with conn:
        cursor = conn.execute(SQL_SELECT_URL_BY_PK, (pk,)) #тут после пк мы ставим зарятую, т.к. так передаются кортежи
        return cursor.fetchone()        

def find_url_by_short(conn, short_url):
    """http://mosa.info/1G5kl"""
    short_url = short_url.rsplit("/", 1).pop()
    pk = inverse(short_url)
    return find_url_by_pk(conn, pk)

def find_url_by_origin(conn, original_url):
    original_url = original_url.strip("/")

    with conn:
        cursor = conn.execute(SQL_SELECT_URL_BY_ORIGIN, (original_url,))
        return cursor.fetchone()

#через вызов функции connect(<имя БД>) подключаемся к БД и используя наши методы - мучаем ее
"""31.05
"""
