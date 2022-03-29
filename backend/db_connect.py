import sqlite3
from sqlite3 import Error


def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect("backend/sqlite.db")
    except Error as e:
        print("ERROR",e)
    
    return conn


def close_connection(conn):
    """ close a database connection to a SQLite database """
    conn.close()

#------------------------------------------------------------------------------

if __name__ == '__main__':
    pass
