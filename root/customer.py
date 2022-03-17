import sqlite3
from sqlite3 import Error
import datetime
import save


def create_customer(name,phone):
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' INSERT INTO customers (name,phone)
            VALUES("{name}","{phone}"); '''
        )
    conn.commit()
    conn.close()
    print(sqlite3.version, "closed")


def create_customer_note(id,note):
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' UPDATE customers
            SET note="{note}"
            WHERE id="{id}"; '''
    )
    conn.commit()
    conn.close()
    print(sqlite3.version, "closed")


def remove_customer(id):
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' DELETE FROM customers
            WHERE id="{id}"; ''' 
    )
    conn.commit()
    conn.close()
    print(sqlite3.version, "closed")
    