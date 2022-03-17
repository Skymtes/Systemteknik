import pricing
import customer
import scuba
import rent
import save


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
