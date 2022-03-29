"""
Module for handeling all things rent
"""

import sqlite3
from sqlite3 import Error

import db_connect


def create_rented(item, fee, customer_id):
    conn = db_connect.create_connection()
    c = conn.cursor()
    c.execute(
        f''' INSERT INTO rented (item,fee,customer_id)
            VALUES("{item}","{fee}","{customer_id}"); '''
        )
    conn.commit()
    conn.close()
    print(sqlite3.version, "closed")


def update_rented(id, item, fee, customer_id):
    conn = db_connect.create_connection()
    c = conn.cursor()
    c.execute(
        f''' UPDATE rented
            SET item="{item}",
            fee="{fee}",
            customer_id="{customer_id}"
            WHERE id="{id}"; '''
    )
    conn.commit()
    conn.close()
    print(sqlite3.version, "closed")


def remove_rented(id):
    conn = db_connect.create_connection()
    c = conn.cursor()
    c.execute(
        f''' DELETE FROM rented
            WHERE id="{id}"; ''' 
    )
    conn.commit()
    conn.close()
    print(sqlite3.version, "closed")
        