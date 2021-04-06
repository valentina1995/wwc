import os
import sqlite3

import logging

logger = logging.getLogger(__name__)

DBPATH = os.path.join(os.path.dirname(__file__), 'restaurant.db')

reservation_config = [
    ('id', 'integer', 'PRIMARY_KEY'),
    ('user_name', 'text', 'NOT NULL'),
    ('identification', 'text', 'NOT NULL'),
    ('phone_number', 'text', 'NOT NULL'),
    ('date', 'text', 'NOT NULL'),
    ('time', 'text', 'NOT NULL'),
    ('num_people', 'text', 'NOT NULL')
]

def db_connect(db_path=DBPATH):
    con = sqlite3.connect(db_path)
    return con


def get_cursor(con):
    return con.cursor()


def create_table(cursor, table_name:str, config:list):
    if not config:
        raise Exception("Cannot create table without proper configuration")
    attrs = ', '.join([f"{item[0]} {item[1]} {item[2]}" for item in config])
    query = f"CREATE TABLE {table_name} ({attrs})"
    logger.info(query)
    return cursor.execute(query)


def get_reservations(cursor, query):
    res = cursor.execute(query).fetchall()
    return res


def create_reservation(cursor, values: tuple):
    query = f"INSERT INTO reservations (id, user_name, identification, phone_number, date, time, num_people) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(query, values)
    return cursor.lastrowid


def table_exists(cursor, table_name:str):
    tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    if not tables:
        return False
    for t in tables:
        if t[0] == table_name:
            return True
    return False

    
