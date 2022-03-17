import sqlite3
from sqlite3 import Error


def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect("pythonsqlite.db")
        print(sqlite3.version, "connected")
    except Error as e:
        print(e)
    
    return conn

#------------------------------------------------------------------------------

if __name__ == '__main__':
    #create_pricelist("UDT")
    #update_pricelist("UDT", "he", 0.5)
    #remove_pricelist("UDT")

    #create_customer("john", "0762332082")
    #create_customer_note("6", "handsome")
    #remove_customer("6")

    pass
