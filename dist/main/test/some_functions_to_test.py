from backend import dbedit_customer as customer
from backend import dbedit_pricing as pricing
from backend import dbedit_scuba as scuba

input("set prices")
pricing.create_pricelist("UDT") #NAME "UDT"
pricing.update_pricelist("UDT", "currency", "SEK")
pricing.update_pricelist("UDT", "service", 100)
pricing.update_pricelist("UDT", "tank", 20)
pricing.update_pricelist("UDT", "air", 0)
pricing.update_pricelist("UDT", "he", 0.5)
pricing.update_pricelist("UDT", "o2", 0.2)

input("create customers")
customer.create_customer("Rickard", "112") #ID 1
customer.create_customer_note(1, "Needs fill by 16/4")
customer.create_customer("Lisa", "911") #ID 2
customer.create_customer_note(2, "Needs fill by 28/3")

input("create tanks")
scuba.create_tank(7, 1) #ID 1
scuba.create_tank(12, 1) #ID 2
scuba.create_tank(15, 1) #ID 3
scuba.create_tank(12, 2) #ID 4

input("set target capacity/mix for tanks")
scuba.set_desired_tank_fill(1, 300, scuba.StandardBlends.AIR)
scuba.set_desired_tank_fill(2, 300, scuba.StandardBlends.EAN(36))
scuba.set_desired_tank_fill(3, 300, scuba.StandardBlends.EAN32)
scuba.set_desired_tank_fill(4, 300, scuba.StandardBlends.Tx(21,20))

input("set current capacity/mix")
scuba.set_tank_fill(1, 0, scuba.StandardBlends.AIR)
scuba.set_tank_fill(2, 0, scuba.StandardBlends.AIR)
scuba.set_tank_fill(3, 0, scuba.StandardBlends.AIR)
scuba.set_tank_fill(4, 0, scuba.StandardBlends.AIR)

input("tankes have been filled")
scuba.fill_tank(1)
scuba.fill_tank(2)
scuba.fill_tank(3)
scuba.fill_tank(4)

input("check debt")
print("person1", pricing.get_debt(1))
print("person2", pricing.get_debt(2))

input("change billing currency and add a fee to the customers")
pricing.update_pricelist("UDT", "currency", "EUR")
pricing.add_service_fee(1)
pricing.add_service_fee(2)

input("check new debt")
print("debt1", pricing.get_debt(1))
print("debt2", pricing.get_debt(2))

input("pay all debts")
pricing.paid_debt(1)
pricing.paid_debt(2)
print("debt1", pricing.get_debt(1))
print("debt2", pricing.get_debt(2))

# input("return tanks")
# scuba.remove_tank(1)
# scuba.remove_tank(2)
# scuba.remove_tank(3)
# scuba.remove_tank(4)



#------------------------------

def ignore():
    # NOT ALLOWED
    pricing.create_pricelist(1)
    pricing.create_pricelist(True)
    pricing.create_pricelist()
    pricing.create_pricelist("")
    pricing.create_pricelist(None)

    pricing.update_pricelist(1, "currency", "SEK")
    pricing.update_pricelist(True, "currency", "SEK")
    pricing.update_pricelist("", "currency", "SEK")
    pricing.update_pricelist(None, "currency", "SEK")

    pricing.update_pricelist("UDT", "currency", None)
    pricing.update_pricelist("UDT", "currency", 1)
    pricing.update_pricelist("UDT", "currency", True)
    pricing.update_pricelist("UDT", "currency", "")
    pricing.update_pricelist("UDT", "service", -1)
    pricing.update_pricelist("UDT", "service", "dsfa")
    pricing.update_pricelist("UDT", "service", None)

    pricing.update_pricelist("UDT", "dasd", "SEK")
    pricing.update_pricelist("UDT", "", "SEK")
    pricing.update_pricelist("UDT", 1, "SEK")
    pricing.update_pricelist("UDT", None, "SEK")
    pricing.update_pricelist("UDT", True, "SEK")