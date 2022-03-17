"""
Module for handeling all things scuba
"""

import datetime
import sqlite3
from sqlite3 import Error

import save
import datetime
import blending
import pricing

class StandardBlends:
    """Standard gas blends, gasmix represented as (oxygen%, helium%)"""
    AIR = (0.21, 0.0)
    EAN32 = (0.32, 0.0)
    EAN36 = (0.36, 0.0)

    def EAN(x):
        if isinstance(x, int) or isinstance(x, float):
            x = x/100
            return (x, 0.0)
        else:
            raise ValueError

    def Tx(o2, he):
        if (isinstance(o2, int) or isinstance(o2, float)) and (isinstance(he, int) or isinstance(he, float)):
            o2 = o2/100
            he = he/100
            return (o2, he)
        else:
            raise ValueError

#CURRENT IMPLEMENTATION CAN NOT USE THIS
class GasPurity:
    """Standard gas blends"""
    # False presumption that both gases are 100% pure
    oxygen = 1
    helium = 1


def create_tank(capacity,customer_id):
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' INSERT INTO tanks (capacity,customer_id)
            VALUES("{capacity}","{customer_id}") '''
    )
    conn.commit()
    conn.close()
    print(sqlite3.version, "closed")


def set_tank_fill(id,pressure,gasmix):
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' UPDATE tanks
            SET pressure="{pressure}",
            gasmix="{gasmix}"
            WHERE id="{id}"; '''
    )
    conn.commit()
    conn.close()
    print(sqlite3.version, "closed")


def set_desired_tank_fill(id,desired_pressure,desired_gasmix):
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' UPDATE tanks
            SET desired_pressure="{desired_pressure}",
            desired_gasmix="{desired_gasmix}"
            WHERE id="{id}"; '''
    )
    conn.commit()
    conn.close()
    print(sqlite3.version, "closed")


def remove_tank(id):
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' DELETE FROM tank
            WHERE id="{id}" ''' 
    )
    conn.commit()
    conn.close()
    print(sqlite3.version, "closed")
    return 


def fill_tank(id):
    raw_tank_data = fetch_tank_data(id)
    tank_data = prepare_data(raw_tank_data)
    print(tank_data[5][0], tank_data[5][1], tank_data[4], tank_data[3][0], tank_data[3][1], tank_data[2]) # DEBUG
    fill = blending.Blend(tank_data[5][0], tank_data[5][1], tank_data[4], tank_data[3][0], tank_data[3][1], tank_data[2])
    print(fill) # DEBUG
    # FIX ALGORITM (needs to take bleeding into account)
    pricing.calculate_tank_price(tank_data[1], fill)


def tank_fill_instructions(id):
    lower_pressure_to = int
    fill_he_to = int
    fill_o2_to = fill_he_to + int
    fill_air_to = fill_o2_to + int


def tank_fill_complete(id):
    time = datetime.datetime.now()
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' UPDATE customers
            SET fill_date="{time}"
            WHERE id="{id}"; '''
    )
    conn.commit()
    conn.close()
    print(sqlite3.version, "closed")


def prepare_data(tank_data):
    tank_data = tank_data[0]
    tank_data = list(tank_data)
    tank_data[3] = tuple(float(s) for s in tank_data[3].strip("()").split(','))
    tank_data[5] = tuple(float(s) for s in tank_data[5].strip("()").split(','))
    tank_data = tuple(tank_data)
    return tank_data


def fetch_tank_data(id):
    conn = save.create_connection()
    c = conn.cursor()
    c.execute(
        f''' SELECT *
            FROM tanks
            WHERE id="{id}"; '''
    )
    tank_data = c.fetchall()
    conn.close()
    print(sqlite3.version, "closed")
    return tank_data
    

if __name__ == '__main__':
#    print("Air: ",StandardBlends.Air)
#    print("32: ",StandardBlends.EAN32)
#    print("36: ",StandardBlends.EAN36)
#    print("100: ",StandardBlends.EAN(100))
#    print("tx air: ",StandardBlends.Tx(21,0))
#    print("tx 50: ",StandardBlends.Tx(10.5,50))
    pass