"""
Module for handeling all things price
"""

import save

class Pricelist:
    """
    An instace of this class represents one stores pricing for their services.
    """

    def __init__(self, name):
        """Price for one metric Liter"""
        self.currency = "SEK" #UNCLEAR HOW CURRENCY TYPE IS BEST CHOOSEN AND STORED. And default currency?

        self.tankfee = 0
        self.servicefee = 0

        self.oxygen = 0
        self.helium = 0
        self.air = 0
    
    def check_ok_input(self, input):
        if isinstance(input, int) or isinstance(input, float):
            return True
        else:
            return False

    def set_currency(self, new_currency):
        self.currency = new_currency

    def set_price_oxygen(self, new_price):
        if self.check_ok_input(new_price) != True:
            raise ValueError    
        self.oxygen = new_price

    def set_price_helium(self, new_price):
        if self.check_ok_input(new_price) != True:
            raise ValueError
        self.helium = new_price

    def set_price_air(self, new_price):
        if self.check_ok_input(new_price) != True:
            raise ValueError    
        self.air = new_price

    def set_price_tankfee(self, new_price):
        """One time cost per tank"""
        if self.check_ok_input(new_price) != True:
            raise ValueError    
        self.tankfee = new_price

    def set_price_servicefee(self, new_price):
        """One time cost per filling"""
        if self.check_ok_input(new_price) != True:
            raise ValueError    
        self.servicefee = new_price

    def tank_total(self, he_l, o2_l, air_l):
        tank_cost = self.tankfee
        print("tank fee", tank_cost)
        tank_cost += he_l*self.helium
        print("tank fee + h", tank_cost)
        tank_cost += o2_l*self.oxygen
        print("tank fee + h + o2", tank_cost)
        tank_cost += air_l*self.air
        print("tank fee + h + o2 + air", tank_cost)
        return tank_cost
        