class Customer:
    """
    An instace of this class represents one customer.
    """

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.to_pay = 0
        self.scubatanks = []
        self.certification = ""

    def add_to_bill(self, amount):
        self.to_pay += amount

    def paid(self):
        self.to_pay = 0

    def remove_customer(self):
        if self.to_pay > 0:
            if input("The customer still has debt of {} which will be deleted. y/n: ".format(self.to_pay)) == "y":
                return True
        else:
            if input("Are you sure? y/n: ") == "y":
                return True
