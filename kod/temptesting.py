"""
This module can be used for various tests that we want to save for later
"""
import scuba
import pricing

# This should later be based on login
my_pricelist = pricing.Pricelist()

#Test tank
capacity = 7 #Liter
pressure = 200 #Bar
gasmix = scuba.StandardBlends.Air #(21, 79, 0)
my_tank = scuba.Tank(capacity, pressure, gasmix)
