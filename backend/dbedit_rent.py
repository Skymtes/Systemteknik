"""
Module for handeling all things rent
"""

import sqlite3

from backend import db_connect


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

def get_rented(customer_id):
    rented_li = {}
    conn = db_connect.create_connection()
    c = conn.cursor()
    c.execute(
        f''' SELECT fee, item, customer_id
            FROM rented
            WHERE customer_id="{customer_id}"; ''' 
    )
    for row in c:
        if row[2] in rented_li.keys():
            rented_li[row[2]].extend([row[0], row[1]])
        else:
            rented_li[row[2]] = [row[0], row[1]]
    conn.commit()
    conn.close()
    return rented_li
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
        