"""
часть 2
"""

import sqlite3
import os.path as path
SQL_SELECT_ALL = """
    SELECT
        id, original_url, short_url, created

    FROM
        shortener
""" #переменные заданные константой - по соглашению - константа. перечисление можно заменить звездочкой. тут мы создаем SQLзапрос

SQL_SELECT_URL_BY_PK = SQL_SELECT_ALL + " WHERE id=?"

SQL_SELECT_URL_BY_ORIGIN = SQL_SELECT_URL_BY_ + " WHERE original_url=?"

SQL_INSERT_URL = """
        INSERT INTO shotener (
        original_url
    )    VALUES (
            ?
    )
"""

#вопросительный знак - неименованный параметр


def connect(db_name = None):
    
    if db_name is None:
        db_name = ":memory:"
        
    conn = sqlite3.connect(db_name)
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
    with conn:
        found = find_url_by_origin(conn, url)
        if found:
            return found[2]
        cursor = conn.execute(SQL_INSERT_URL, (url,))
        #здесь магия
        return

def findall(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()


def find_url_by_pk(conn, pk):
    with conn:
        cursor = conn.execute(SQL_SELECT_URL_BY_PK, (pk,)) #тут после пк мы ставим зарятую, т.к. так передаются кортежи
        return cursor.fetchone()        

def find_url_by_short(conn, short_url):
    #здесь будет магия
    pass


def find_url_by_origin(conn, original_url):
    original_url = original_url.strip("/")

    with conn:
        cursor = conn.execute(SQL_SELECT_URL_BY_ORIGIN, (original_url,))
        return cursor.fetchone()

#через вызов функции connect(<имя БД>) подключаемся к БД и используя наши методы - мучаем ее
