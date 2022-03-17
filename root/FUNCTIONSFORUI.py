import pricing
import scuba
import json
import save
import customer

#--- Connect to UI ------------------------------------------------------------
#CREATE pricelist
pricing.create_pricelist(INPUT_STRING) #Input is the name of the pricelist (UNIQUE!)

#EDIT pricelist
#First input is name of the pricelist, second is just what to change, third is what it will be changed to
pricing.update_pricelist(INPUT_STRING, "currency", INPUT_STRING) #desired currency
pricing.update_pricelist(INPUT_STRING, "tank", INPUT_INT) #fee per tank
pricing.update_pricelist(INPUT_STRING, "service", INPUT_INT) #fee per filling
pricing.update_pricelist(INPUT_STRING, "air", INPUT_INT) #price of air per liter
pricing.update_pricelist(INPUT_STRING, "he", INPUT_INT) #price of helium per liter
pricing.update_pricelist(INPUT_STRING, "o2", INPUT_INT) #price of oxygen per liter

#REMOVE pricelist
pricing.remove_pricelist(INPUT_STRING) #removes specified pricelist (need way to get name of list)
#------------------------------------------------------------------------------



#--- Connect to UI ------------------------------------------------------------
#CREATE customer
customer.create_customer(INPUT_STRING, INPUT_STRING) #First is customer name, second is phone nr

#EDIT customer
customer.create_customer_note(INPUT_STRING) #Input is a note related to customer

#REMOVE customer
customer.remove_customer(INPUT_INT) #Input is ID of customer (need way to get id from database)
#------------------------------------------------------------------------------



#--- Connect to UI ------------------------------------------------------------
#CREATE tank
#First is tank capacity, second is pressure, third gasmix (oxygen%, helium%), fourth customer_id
scuba.create_tank(INPUT_INT, INPUT_INT, INPUT_STRING, INPUT_INT) 

#EDIT tank
#Sets new fill target
scuba.set_tank_fill(INPUT_INT, INPUT_STRING) #First is pressure, second gasmix

#Call when fill is done
scuba.tank_filled(INPUT_INT,INPUT_INT,INPUT_STRING) #First is id, second new pressure, third new mix (oxygen%, helium%)

#REMOVE tank
scuba.remove_tank(INPUT_INT) #Input is ID of tank (need way to get id from database)
#------------------------------------------------------------------------------
