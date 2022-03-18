import pricing
import customer
import scuba
import save


#     # First Boot of App (only run once per install)
# pricing.create_pricelist("UDT") #NAME "UDT"

#     # Setting up prices
# pricing.update_pricelist("UDT", "currency", "SEK")
# pricing.update_pricelist("UDT", "service", 100)
# pricing.update_pricelist("UDT", "tank", 20)
# pricing.update_pricelist("UDT", "air", 0)
# pricing.update_pricelist("UDT", "he", 0.5)
# pricing.update_pricelist("UDT", "o2", 0.2)

#     # Creating customers and adding notes to them
# customer.create_customer("Rickard", "112") #ID 1
# customer.create_customer_note(1, "Needs fill by 16/4")
# customer.create_customer("Lisa", "911") #ID 2
# customer.create_customer_note(2, "Needs fill by 28/3")

#     # When a customer gives you a tank to fill
# scuba.create_tank(7, 1) #ID 1
# scuba.create_tank(12, 1) #ID 2
# scuba.create_tank(15, 1) #ID 3
# scuba.create_tank(12, 2) #ID 4
# scuba.create_tank(15, 2) #ID 5
# scuba.create_tank(15, 2) #ID 6
# scuba.create_tank(7, 2) #ID 7

    # setting the new desired blend for a tank
scuba.set_desired_tank_fill(1, 300, scuba.StandardBlends.AIR)
scuba.set_desired_tank_fill(2, 300, scuba.StandardBlends.EAN(36))
scuba.set_desired_tank_fill(3, 300, scuba.StandardBlends.EAN32)
scuba.set_desired_tank_fill(4, 300, scuba.StandardBlends.Tx(21,20))

    # when you have analysed the tanks contents
scuba.set_tank_fill(1, 0, scuba.StandardBlends.AIR)
scuba.set_tank_fill(2, 0, scuba.StandardBlends.AIR)
scuba.set_tank_fill(3, 0, scuba.StandardBlends.AIR)
scuba.set_tank_fill(4, 0, scuba.StandardBlends.AIR)

    # fills the tank to desired mix and pressure, and updates the tanks cost in database
scuba.fill_tank(1)
scuba.fill_tank(2)
scuba.fill_tank(3)
scuba.fill_tank(4)

    # get customer debt (a dictionary with every currency as key and amount as value)
print("debt1", pricing.get_debt(1))
print("debt2", pricing.get_debt(2))

#     # When you want to add a service fee to a customer
# pricing.add_service_fee(1)
# pricing.add_service_fee(2)

    # When a customer has paid
pricing.paid_debt(1)
pricing.paid_debt(2)

#     # When you return a tank to the customer
# scuba.remove_tank(1)
# scuba.remove_tank(2)
# scuba.remove_tank(3)
# scuba.remove_tank(4)
# scuba.remove_tank(5)
# scuba.remove_tank(6)
# scuba.remove_tank(7)


# customer.remove_customer(1)
# pricing.remove_pricelist("UDT")
