"""
This module can be used for various tests that we want to save for later
"""
import scuba
import pricing

# This should later be based on login
my_pricelist = pricing.Pricelist()

#Test tank
capacity = 7 #Liter
pressure = 102 #Bar
gasmix = scuba.StandardBlends.EAN36 #(36, 64, 0)
my_tank = scuba.Tank(capacity, pressure, gasmix)

my_tank.set_desired_pressure(200)
my_tank.set_desired_gasmix(scuba.StandardBlends.EAN(28))

my_tank.fill()
