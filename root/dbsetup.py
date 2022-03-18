"""
Commands for setting up sqlite db
"""

import sqlite3
from sqlite3 import Error

import save


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    pricelists_table = """ CREATE TABLE IF NOT EXISTS pricelists (
                                    name text PRIMARY KEY,
                                    currency text,
                                    o2 int,
                                    he int,
                                    air int,
                                    tank int,
                                    service int
                                ); """

    customers_table = """ CREATE TABLE IF NOT EXISTS customers (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    name text NOT NULL,
                                    phone text NOT NULL,
                                    note text
                                ); """

    tanks_table = """ CREATE TABLE IF NOT EXISTS tanks (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    capacity integer NOT NULL,
                                    pressure integer,
                                    gasmix text,
                                    desired_pressure integer,
                                    desired_gasmix text,
                                    fill_date text,
                                    fill_cost integer,
                                    customer_id integer NOT NULL,
                                    FOREIGN KEY (customer_id) REFERENCES customer (id)
                                ); """
                            
    payments_table = """ CREATE TABLE IF NOT EXISTS payments (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    customer_id integer NOT_NULL,
                                    amount integer NOT NULL,
                                    bill_date text,
                                    paid_date text,
                                    paid integer NOT NULL,
                                    currency text,
                                    FOREIGN KEY (customer_id) REFERENCES customer (id)
                                ); """
                            
    rented_table = """ CREATE TABLE IF NOT EXISTS rented (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    item text NOT NULL,
                                    item_fee integer NOT NULL,
                                    customer_id integer NOT NULL,
                                    FOREIGN KEY (customer_id) REFERENCES customer (id)
                                ); """

    # create a database connection
    conn = save.create_connection()

    # create tables
    if conn is not None:
        create_table(conn, pricelists_table)
        create_table(conn, customers_table)
        create_table(conn, tanks_table)
        create_table(conn, payments_table)
        create_table(conn, rented_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()