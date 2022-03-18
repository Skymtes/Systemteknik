"""
Module for handeling all things price
"""

import sqlite3
from sqlite3 import Error
import datetime

import save

def create_pricelist(name):
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' INSERT INTO pricelists (name)
            VALUES("{name}"); '''
        )
    conn.commit()
    save.close_connection(conn)


def update_pricelist(name, type, price):
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' UPDATE pricelists
            SET {type}="{price}"
            WHERE name="{name}"; '''
    )
    conn.commit()
    save.close_connection(conn)


def remove_pricelist(name):
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' DELETE FROM pricelists
            WHERE name="{name}"; ''' 
    )
    conn.commit()
    save.close_connection(conn)

#--------------------------------------------------------------------

def create_payment(customer_id, amount):
    time = datetime.datetime.now()
    currency = fetch_currency()
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' INSERT INTO payments (customer_id, amount, bill_date, paid, currency)
            VALUES("{customer_id}","{amount}","{time}","{0}","{currency}"); '''
        )
    conn.commit()
    save.close_connection(conn)


def add_service_fee(customer_id):
    time = datetime.datetime.now()
    currency = fetch_currency()
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' SELECT service FROM pricelists
            WHERE name="UDT"; '''
        )
    service_fee = c.fetchall()[0][0]
    c.execute(
        f''' INSERT INTO payments (customer_id, amount, bill_date, paid, currency)
            VALUES("{customer_id}","{service_fee}","{time}","{0}","{currency}"); '''
        )
    conn.commit()
    save.close_connection(conn)


def get_debt(customer_id):
    time = datetime.datetime.now()
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' SELECT DISTINCT currency FROM payments
            WHERE customer_id="{customer_id}"
            AND paid="{0}"; '''
        )
    currencies = c.fetchall()
    
    debts = {}
    for currency in currencies:
        debts[currency[0]] = 0

    for currency in currencies:
        c.execute(
            f''' SELECT amount FROM payments
                WHERE customer_id="{customer_id}"
                AND paid="{0}"
                AND currency="{currency[0]}"; '''
            )
        amounts = c.fetchall()
        for amount in amounts:
            debts[currency[0]] += amount[0]
    
    for currency in currencies:
        debts[currency[0]] = round(debts[currency[0]], 3)

    save.close_connection(conn)
    return debts


def paid_debt(customer_id):
    time = datetime.datetime.now()
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' UPDATE payments
            SET paid="{1}",
            paid_date="{time}"
            WHERE customer_id="{customer_id}"; '''
    )
    conn.commit()
    save.close_connection(conn)

#--------------------------------------------------------------------

def calculate_tank_price(capacity, fill):
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' SELECT o2, he, air FROM pricelists
            WHERE name="UDT"; '''
        )
    prices = c.fetchall()[0]
    print("price/l o2 he air",prices)
    print("tank capacity",capacity)
    o2_cost = round(fill[0]*capacity*prices[0], 3)
    he_cost = round(fill[1]*capacity*prices[1], 3)
    air_cost = round(fill[2]*capacity*prices[2], 3)
    print("cost of o2 he air tankfee",o2_cost, he_cost, air_cost, fetch_tank_fee())
    return o2_cost + he_cost + air_cost + fetch_tank_fee()


def fetch_tank_fee():
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' SELECT tank FROM pricelists
            WHERE name="UDT"; '''
    )
    tank_fee = c.fetchall()
    save.close_connection(conn)
    return tank_fee[0][0]


def fetch_currency():
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' SELECT currency FROM pricelists
            WHERE name="UDT"; '''
    )
    currency = c.fetchall()
    save.close_connection(conn)
    return currency[0][0]
