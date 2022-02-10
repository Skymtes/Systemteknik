"""
This module can be used for various tests that we want to save for later
"""

import pricing

my_pricelist = pricing.Pricelist()
my_pricelist.set_price_oxygen(3)
print(my_pricelist.oxygen)