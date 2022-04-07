import sqlite3
from sqlite3 import Error
import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend import db_connect


def create_customer(name,phone,email,type,date):
    conn = db_connect.create_connection()
    c = conn.cursor()
    c.execute(
        f''' INSERT INTO customers (name,phone,email,type,date)
            VALUES("{name}","{phone}","{email}","{type}","{date}"); '''
        )
    conn.commit()
    db_connect.close_connection(conn)
def find_id(name):
    conn = db_connect.create_connection()
    c = conn.cursor()
    c.execute(
        f''' SELECT id
            FROM customers
            WHERE name="{name}"; '''
        )
    for row in c:
        return(row[0])
    db_connect.close_connection(conn)

def create_customer_note(id,note):
    conn = db_connect.create_connection()
    c = conn.cursor()
    c.execute(
        f''' UPDATE customers
            SET note="{note}"
            WHERE id="{id}"; '''
    )
    conn.commit()
    db_connect.close_connection(conn)

def select_customer():
    customer_li = []
    conn = db_connect.create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM customers')
    for row in c:
        #print(row)
        customer_li.append(row)
    return(customer_li)

def remove_customer(id):
    """DONT!!!"""
    conn = db_connect.create_connection()
    c = conn.cursor()
    c.execute(
        f''' DELETE FROM customers
            WHERE id="{id}"; ''' 
    )
    conn.commit()
    db_connect.close_connection(conn)
#remove_customer(9)
#create_customer("AHmad",56789,"ahmad@amt.com","Nitrox",datetime.date.today())
#select_customer()