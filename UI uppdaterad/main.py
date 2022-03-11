from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.properties import ObjectProperty
from kivy.uix.checkbox import CheckBox



class HomeScreen(Screen):
    old_pressure = ObjectProperty(None)
    old_ntwo = ObjectProperty(None)
    old_he = ObjectProperty(None)
    old_otwo = ObjectProperty(None)

    new_otwo = ObjectProperty(None) 
    new_ntwo = ObjectProperty(None)
    new_he = ObjectProperty(None)
    new_pressure = ObjectProperty(None)




    def btn(self):
        pass 

        

class SettingsScreen(Screen):

    price_oxygen = ObjectProperty(None)
    price_nitrogen = ObjectProperty(None)
    price_helium = ObjectProperty(None)
    price_service_fee = ObjectProperty(None) 
    price_tank_fee = ObjectProperty(None)
    cylinder_size = ObjectProperty(None)
    cyliner_maximum_pressure = ObjectProperty(None)

    def button(self):
        # pricing.update_pricelist(INPUT_STRING, "currency", INPUT_STRING) #desired currency...... Ska man få välja vilken valuta eller bara ha SEK?
        # pricing.update_pricelist(INPUT_STRING, "tank", self.price_tank_fee.text) #fee per tank
        # pricing.update_pricelist(INPUT_STRING, "service", self.price_service_fee.text) #fee per filling
        # pricing.update_pricelist(INPUT_STRING, "air", self.price_nitrogen.text) #price of air per liter..... Priset på nitrogen 
        # pricing.update_pricelist(INPUT_STRING, "he", self.price_helium.text) #price of helium per liter
        # pricing.update_pricelist(INPUT_STRING, "o2", self.price_oxygen.text)
        #parameter för max-size på cylinder
        #parameter för storleken på cylinder
        pass 
    


    

class SelectCustomerScreen(Screen):
    pass




class AddProfileScreen(Screen):
    pass






class TableScreen(Screen):
    pass 





class ImageButton(ButtonBehavior, Image):
    pass






class ProfileScreen(Screen):
    pass 





class MoreInfoScreen(Screen):
    pass





GUI = Builder.load_file('main.kv')
class MainApp(App):
    def build(self):
        return GUI
    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name
        



MainApp().run()