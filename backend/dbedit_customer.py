from backend import db_connect


def create_customer(name,phone,email,cert,date):
    conn = db_connect.create_connection()
    c = conn.cursor()
    c.execute(
        f''' INSERT INTO customers (name,phone,email,cert,date)
            VALUES("{name}","{phone}","{email}","{cert}","{date}"); '''
        )
    conn.commit()
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


def update_customer(id, type, price):
    conn = db_connect.create_connection()
    c = conn.cursor()
    c.execute(
        f''' UPDATE customers
            SET {type}="{price}"
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


def remove_customer(id):
    """
    will lose track of tanks, rented items and payments
    so make sure all tanks, rented items are returned and all payments complete
    """
    conn = db_connect.create_connection()
    c = conn.cursor()
    c.execute(
        f''' DELETE FROM rented
            WHERE customer_id="{id}"; ''' 
    )
    c.execute(
        f''' DELETE FROM payments
            WHERE customer_id="{id}"; ''' 
    )
    c.execute(
        f''' DELETE FROM tanks
            WHERE customer_id="{id}"; ''' 
    )
    c.execute(
        f''' DELETE FROM customers
            WHERE id="{id}"; ''' 
    )
    conn.commit()
    db_connect.close_connection(conn)
