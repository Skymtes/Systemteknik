"""
This module can be used for various tests that we want to save for later
"""
import scuba
import pricing
import customer

my_pricelist = pricing.Pricelist()
customers = []

# This should later be based on login
# Creating a customized pricelist and sets prices for gases and currency type
my_pricelist.set_currency("SEK")
my_pricelist.set_price_tankfee(50)
my_pricelist.set_price_servicefee(100)
my_pricelist.set_price_helium(0.5)
my_pricelist.set_price_oxygen(0.1)
my_pricelist.set_price_air(0.0)

# Creating two customers and their tanks
customers.append(customer.Customer("John", "112"))
customer_1 = customers[0]

customers.append(customer.Customer("Lisa", "911"))
customer_2 = customers[1]


customer_1.scubatanks.append(scuba.Tank(7, 0, scuba.StandardBlends.Air, 200, scuba.StandardBlends.Air))
customer_1.scubatanks.append(scuba.Tank(12, 0, scuba.StandardBlends.Air, 300, scuba.StandardBlends.Air))

customer_2 = customer.Customer("Lisa", "911")
customer_2.scubatanks.append(scuba.Tank(10, 0, scuba.StandardBlends.Air, 200, scuba.StandardBlends.Tx(10.5,50)))
customer_2.scubatanks.append(scuba.Tank(10, 0, scuba.StandardBlends.Air, 200, scuba.StandardBlends.Tx(30,70)))


# Fill customers tanks
for i, j in enumerate(customer_1.scubatanks):
    h_l, o2_l, air_l = customer_1.scubatanks[i].trimix_empty_tank()
    tank_cost = my_pricelist.tank_total(h_l, o2_l, air_l)
    customer_1.add_to_bill(tank_cost)
customer_1.add_to_bill(my_pricelist.servicefee)


for i, j in enumerate(customer_2.scubatanks):
    h_l, o2_l, air_l = customer_2.scubatanks[i].trimix_empty_tank()
    tank_cost = my_pricelist.tank_total(h_l, o2_l, air_l)
    customer_2.add_to_bill(tank_cost)
customer_2.add_to_bill(my_pricelist.servicefee)


# Customers pay their bills
# Terrible implemen
print(customer_1.name, "Total to be paid", customer_1.to_pay, my_pricelist.currency)
customer_1.paid()
if customer_1.remove_customer() == True:
    customers.remove(customer_1)

print(customer_2.name, "Total to be paid", customer_2.to_pay, my_pricelist.currency)
if customer_2.remove_customer() == True:
    customers.remove(customer_2)
customer_2.paid()

print(customers)
