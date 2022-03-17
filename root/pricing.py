"""
Module for handeling all things price
"""

import sqlite3
from sqlite3 import Error

import save

def create_pricelist(name):
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' INSERT INTO pricelists (name)
            VALUES("{name}"); '''
        )
    conn.commit()
    conn.close()
    print(sqlite3.version, "closed")


def update_pricelist(name, type, price):
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' UPDATE pricelists
            SET {type}="{price}"
            WHERE name="{name}"; '''
    )
    conn.commit()
    conn.close()
    print(sqlite3.version, "closed")


def remove_pricelist(name):
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' DELETE FROM pricelists
            WHERE name="{name}"; ''' 
    )
    conn.commit()
    conn.close()
    print(sqlite3.version, "closed")

#--------------------------------------------------------------------

def create_payment(customer_id, amount):
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' INSERT INTO payments (customer_id, amount, paid)
            VALUES("{customer_id}","{amount}","{0}"); '''
        )
    conn.commit()
    conn.close()
    print(sqlite3.version, "closed")

#--------------------------------------------------------------------

def calculate_tank_price(capacity, fill):
    o2_cost = fill[0]*capacity
    he_cost = fill[1]*capacity
    air_cost = fill[2]*capacity
    return o2_cost + he_cost + air_cost
