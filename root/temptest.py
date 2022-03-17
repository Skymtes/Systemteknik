import pricing
import customer
import scuba
import rent
import save

"""
"""
pricing.create_pricelist("UDT") #NAME "UDT"
pricing.update_pricelist("UDT", "currency", "SEK")
pricing.update_pricelist("UDT", "service", 100)
pricing.update_pricelist("UDT", "tank", 20)
pricing.update_pricelist("UDT", "air", 0)
pricing.update_pricelist("UDT", "he", 0.5)
pricing.update_pricelist("UDT", "o2", 0.2)


customer.create_customer("Daniel", "112") #ID 1
customer.create_customer_note(1, "Needs fill by 16/4")
customer.create_customer("Lisa", "911") #ID 2
customer.create_customer_note(2, "Needs fill by 28/3")


scuba.create_tank(7, 1) #ID 1
scuba.set_tank_fill(1, 300, scuba.StandardBlends.AIR)

scuba.create_tank(12, 1) #ID 2
scuba.set_tank_fill(2, 300, scuba.StandardBlends.EAN(36))

scuba.create_tank(12, 1) #ID 3
scuba.set_tank_fill(3, 300, scuba.StandardBlends.EAN32)

scuba.create_tank(7, 2) #ID 4
scuba.set_tank_fill(4, 0, scuba.StandardBlends.AIR)

scuba.create_tank(15, 2) #ID 5
scuba.set_tank_fill(5, 0, scuba.StandardBlends.AIR)
scuba.set_tank_fill(5, 200, scuba.StandardBlends.Tx(10.5, 50))

scuba.create_tank(15, 2) #ID 6
scuba.set_tank_fill(6, 200, scuba.StandardBlends.AIR)

scuba.create_tank(7, 2) #ID 7
scuba.set_tank_fill(7, 300, scuba.StandardBlends.Tx(15, 80))

scuba.tank_fill(1)
scuba.tank_fill(2)
scuba.tank_fill(3)
scuba.tank_fill(4)
scuba.tank_fill(5)
scuba.tank_fill(6)
scuba.tank_fill(7)

"""

tank_fill_complete(1)
tank_fill_complete(2)
tank_fill_complete(3)
tank_fill_complete(4)
tank_fill_complete(5)
tank_fill_complete(6)
tank_fill_complete(7)
set_tank_fill(1,measured_pressure, measured_gasmix)
set_tank_fill(2,measured_pressure, measured_gasmix)
set_tank_fill(3,measured_pressure, measured_gasmix)
set_tank_fill(4,measured_pressure, measured_gasmix)
set_tank_fill(5,measured_pressure, measured_gasmix)
set_tank_fill(6,measured_pressure, measured_gasmix)
set_tank_fill(7,measured_pressure, measured_gasmix)
"""
"""
scuba.tank_filled(INPUT_INT,INPUT_INT,INPUT_STRING)
scuba.remove_tank(INPUT_INT)
"""
#------------------------------------------------------------------------------

#pricing.remove_pricelist("UDT")
#customer.remove_customer(1)
