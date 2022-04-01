import unittest
import sys
import os
import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.db_connect import create_connection, close_connection
from backend.db_setup import main
from backend.dbedit_customer import create_customer, create_customer_note
from backend.dbedit_pricing import create_pricelist, update_pricelist, remove_pricelist, create_payment, add_service_fee, get_debt, paid_debt, calculate_tank_price, fetch_tank_fee, fetch_currency
from backend.dbedit_scuba import create_tank, set_tank_fill, set_desired_tank_fill, remove_tank, fill_tank, tank_fill_complete, prepare_data, fetch_tank_data
from backend import dbedit_customer as customer
from backend import dbedit_pricing as pricing
from backend import dbedit_scuba as scuba


class DatabaseTest(unittest.TestCase):

    main()

    def test_connection(self):
        conn = create_connection()
        assert conn is not None

    def test_connection_close(self):
        conn = create_connection()
        closed_conn = close_connection(conn)
        assert closed_conn is None

    def test_2create_customer(self):
        conn = create_connection()
        c = conn.cursor()
        customer.create_customer("Rickard", "112") #ID 1
        customer.create_customer("Lisa", "911") #ID 2
        c.execute(f'''SELECT * FROM customers''')
        customers = c.fetchall()
        self.assertEqual(customers, [(1, 'Rickard', '112', None), (2, 'Lisa', '911', None)])
        close_connection(conn)
        
    def test_3create_customer_note(self):
        conn = create_connection()
        c = conn.cursor()
        customer.create_customer_note(1, "Needs fill by 16/4")
        customer.create_customer_note(2, "Needs fill by 28/3")
        c.execute(f'''SELECT * FROM customers''')
        customer_note = c.fetchall()
        self.assertEqual(customer_note, [(1, 'Rickard', '112', 'Needs fill by 16/4'), (2, 'Lisa', '911', 'Needs fill by 28/3')])
        close_connection(conn)

    def test_1pricelist(self):
        conn = create_connection()
        c = conn.cursor()
        pricing.create_pricelist("UDT") #NAME "UDT"
        pricing.update_pricelist("UDT", "currency", "SEK")
        pricing.update_pricelist("UDT", "service", 100)
        pricing.update_pricelist("UDT", "tank", 20)
        pricing.update_pricelist("UDT", "air", 0)
        pricing.update_pricelist("UDT", "he", 0.5)
        pricing.update_pricelist("UDT", "o2", 0.2)
        c.execute(f'''SELECT * FROM pricelists''')
        pricelist = c.fetchall()
        self.assertEqual(pricelist, [('UDT', 'SEK', 0.2, 0.5, 0, 20, 100)])
        close_connection(conn)

    def test_8get_debt(self):
        x = pricing.get_debt(1)
        y = pricing.get_debt(2)
        self.assertEqual(x, {'SEK': 322.2})
        self.assertEqual(y, {'SEK': 418.16})

    def test_9add_service_fee(self):
        pricing.add_service_fee(1)
        pricing.add_service_fee(2)

    def test_10paid_debt(self):
        pricing.paid_debt(1)
        pricing.paid_debt(2)
        x = pricing.get_debt(1)
        y = pricing.get_debt(2)
        self.assertEqual(x, {})
        self.assertEqual(y, {})

    def test_fetch_tank_fee(self):
        fee = pricing.fetch_tank_fee()
        self.assertEqual(fee, 20)

    def test_fetch_currency(self):
        fee = pricing.fetch_currency()
        self.assertEqual(fee, "SEK")

    def test_4create_tank(self):
        scuba.create_tank(7, 1) #ID 1
        scuba.create_tank(12, 1) #ID 2
        scuba.create_tank(15, 1) #ID 3
        scuba.create_tank(12, 2) #ID 4
        conn = create_connection()
        c = conn.cursor()
        c.execute(f'''SELECT * FROM tanks''')
        pricelist = c.fetchall()
        close_connection(conn)
        self.assertEqual(pricelist, [(1, 7, None, None, None, None, None, None, 1), (2, 12, None, None, None, None, None, None, 1), (3, 15, None, None, None, None, None, None, 1), (4, 12, None, None, None, None, None, None, 2)])

    def test_6set_tank_fill(self):
        scuba.set_tank_fill(1, 0, scuba.StandardBlends.AIR)
        scuba.set_tank_fill(2, 0, scuba.StandardBlends.AIR)
        scuba.set_tank_fill(3, 0, scuba.StandardBlends.AIR)
        scuba.set_tank_fill(4, 0, scuba.StandardBlends.AIR)
        conn = create_connection()
        c = conn.cursor()
        c.execute(f'''SELECT * FROM tanks''')
        pricelist = c.fetchall()
        close_connection(conn)
        self.assertEqual(pricelist, [(1, 7, 0, '(0.21, 0.0)', 300, '(0.21, 0.0)', None, None, 1), (2, 12, 0, '(0.21, 0.0)', 300, '(0.36, 0.0)', None, None, 1), (3, 15, 0, '(0.21, 0.0)', 300, '(0.32, 0.0)', None, None, 1), (4, 12, 0, '(0.21, 0.0)', 300, '(0.21, 0.2)', None, None, 2)])

    def test_5set_desired_tank_fill(self):
        scuba.set_desired_tank_fill(1, 300, scuba.StandardBlends.AIR)
        scuba.set_desired_tank_fill(2, 300, scuba.StandardBlends.EAN(36))
        scuba.set_desired_tank_fill(3, 300, scuba.StandardBlends.EAN32)
        scuba.set_desired_tank_fill(4, 300, scuba.StandardBlends.Tx(21,20))
        conn = create_connection()
        c = conn.cursor()
        c.execute(f'''SELECT * FROM tanks''')
        pricelist = c.fetchall()
        close_connection(conn)
        self.assertEqual(pricelist, [(1, 7, None, None, 300, '(0.21, 0.0)', None, None, 1), (2, 12, None, None, 300, '(0.36, 0.0)', None, None, 1), (3, 15, None, None, 300, '(0.32, 0.0)', None, None, 1), (4, 12, None, None, 300, '(0.21, 0.2)', None, None, 2)])

    def test_fetch_currency(self):
        scuba.remove_tank(1)
        conn = create_connection()
        c = conn.cursor()
        c.execute(f'''SELECT id FROM tanks''')
        pricelist = c.fetchall()
        close_connection(conn)
        self.assertEqual(pricelist, [(2,), (3,), (4,)])

    def test_7fill_tank(self):
        scuba.fill_tank(1)
        scuba.fill_tank(2)
        scuba.fill_tank(3)
        scuba.fill_tank(4)

    def test_remove_pricelist(self):
        conn = create_connection()
        c = conn.cursor()
        pricing.remove_pricelist("UDT")
        c.execute(f'''SELECT * FROM pricelists''')
        pricelist = c.fetchall()
        close_connection(conn)
        self.assertEqual(pricelist, [])

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = unittest.TestLoader().loadTestsFromTestCase(DatabaseTest)
    runner.run(suite)

