import pricing
import json

def firstboot():
    """Will be run the first time the app is started"""

    # Enter your prices
    my_pricelist = pricing.Pricelist()
    #--- CONNECT TO UI ---
    my_pricelist.set_currency(INPUT_STRING) 
    my_pricelist.set_price_tankfee(INPUT_INT)
    my_pricelist.set_price_servicefee(INPUT_INT)
    my_pricelist.set_price_helium(INPUT_INT)
    my_pricelist.set_price_oxygen(INPUT_INT)
    my_pricelist.set_price_air(INPUT_INT)
    #---------------------

    firstbootdone(my_pricelist)

def firstbootdone(my_pricelist):
    with open("pricelist.json", "w") as fp:
        json.dump(my_pricelist, fp)

    with open("settings.json", "w") as fp:
        json.dump({"firstboot": False}, fp)