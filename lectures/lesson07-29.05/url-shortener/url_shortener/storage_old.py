"""
часть 1
1. Устанговка соединения.
-адрес, логин, пароль
2. Выбор БазыДанных с которой мы будем работать
предыдущие два пункта не для sqlite

А с sqlite - один файл - одна база данных
1. Выбор файла, с которым мы хотим работать
2. Создание объекта-курсора (все взаимодействия с базой проходят через взаимодействие с курсором?)
3.Выполнение SQL-запросов(много!))
    Виды запросов:
    -изменение состояния БД
    CREATE TABLE...... - создание таблиц
    -выборка (получение) данных из БД
    SELECT
4. Закрыть соединение!!!

первичный ключ - уникальный идентификатор - Primary Key (PK) - уникальный ключ в таблице, по которому можно однозначно идентифицировать одну строку
Как правило СУБД генерирует его автоматически. Система обычно называт его id (как правило - это целое число). AUTOINCREMENT - указывает на то, что будет
создаваться автоматически

описание колонок разделяется запятой
PEP8  в помощь
фактически sqlite хранит все в строках
нет контроля по ключам
есть такое зарезервированное солов как NOT NULL, если его опустить, то NULL может быть, а это не удобно


ORM - объект релэйшн мэппинг (может сделать все)
PonyORM - сделали реализацию join-ов 
"""
import sqlite3

conn = sqlite3.connect(":memory:") #1метод коннект принимает в нашем случае файл, но с другим базами данных как раз login, пароль

cursor = conn.cursor() #2чтобы создать курсор, нужно воспользоваться коннектом, курсор тоже нужно закрывать

sql = """
    CREATE TABLE IF NOT EXIST shortener(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_url TEXT NOT NULL,
        short_url TEXT NOT NULL DEFAULT "",
        created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,               
    )
"""#3)эта строка - это запрос на создание шапки таблицы, собсна. чтобы выполнить запрос нам нужен созданный курсор

#cursor.execute(sql) #выполняет один запрос
cursor.executscript(sql) #выполняет SQL-скрипт (это как запрос, только их много и они чере точку с запятой

conn.close() #4) connect - это было открытие (как файла) в конце работы с БД нужно будет закрыть

