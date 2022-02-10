"""
Module for handeling all things price
"""

class Pricelist:
    """
    An instace of this class represents one stores pricing for their services.
    """

    def __init__(self):
        self.oxygen = None
        self.helium = None
        self.air = None

        self.startingfee = None
        self.servicefee = None
    
    def check_ok_input(self, input):
        if isinstance(input, int):
            return True
        else:
            return False

    def set_price_oxygen(self, new_price):
        if self.check_ok_input(new_price) != True:
            raise ValueError
        
        self.oxygen = new_price
