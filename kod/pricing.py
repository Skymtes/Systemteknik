"""
Module for handeling all things price
"""

class Pricelist:
    """
    An instace of this class represents one stores pricing for their services.
    """

    def __init__(self):
        """Price for one metric Liter"""
        self.oxygen = 0
        self.helium = 0
        self.air = 0

        self.startingfee = 0
        self.servicefee = 0
    
    def check_ok_input(self, input):
        if isinstance(input, int):
            return True
        else:
            return False

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

    def set_price_startingfee(self, new_price):
        if self.check_ok_input(new_price) != True:
            raise ValueError    
        self.startingfee = new_price

    def set_price_servicefee(self, new_price):
        if self.check_ok_input(new_price) != True:
            raise ValueError    
        self.servicefee = new_price
