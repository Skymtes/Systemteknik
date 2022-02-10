class Pricelist:
    def __init__(self):
        self.oxygen = None
        self.helium = None
        self.air = None

        self.startingfee = None
        self.servicefee = None
    
    def check_ok_input(self, input)
        if isinstance(input, int):
            return True
        else:
            return False

    def set_price_oxygen(self, new_price):
        if check_ok_input(new_price) != True:
            raise ValueError
        
        self.oxygen = new_price
