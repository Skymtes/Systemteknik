from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.properties import ObjectProperty
from kivy.uix.checkbox import CheckBox
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from backend.algorithm import blending as blending
from backend import db_connect, dbedit_customer, dbedit_pricing, dbedit_rent, dbedit_scuba


class HomeScreen(Screen):
    old_pressure = ObjectProperty(None)
    old_he = ObjectProperty(None)
    old_otwo = ObjectProperty(None)

    new_otwo = ObjectProperty(None)
    new_he = ObjectProperty(None)
    new_pressure = ObjectProperty(None)




    def btn(self):
        
        if self.ids.old_pressure.text == '' and self.ids.old_he.text == '' and self.ids.old_otwo.text == '' and self.ids.new_otwo.text == '' and self.ids.new_he.text == '' and self.ids.new_pressure.text == '':
            
            self.manager.get_screen('more_info_screen')
        else:
            a = Blending.Blend( (float(self.new_otwo.text))/100, (float(self.new_he.text))/100, float(self.new_pressure.text), (float(self.old_otwo.text))/100, (float(self.old_he.text))/100, float(self.old_pressure.text)) #Values should be enterd in Procents/Bar. 
            self.manager.get_screen('more_info_screen').change_values(a, self.new_otwo.text,self.new_he.text,self.new_pressure.text,self.old_otwo.text,self.old_he.text,self.old_pressure.text)
            self.ids.old_pressure.text = ' '
            self.ids.old_he.text = ' '
            self.ids.old_otwo.text = ' '
            self.ids.new_otwo.text = ' '
            self.ids.new_he.text = ' '
            self.ids.new_pressure.text = ' '

        

class SettingsScreen(Screen):

    _currency = None

    def spinnerclick(self, value):
        self._currency = value

    def button(self):
        pass


        
        # self.ids.cylinder_size.text = ''
        # self.cyliner_maximum_pressure.text = ''

    def confirm(self):

        self._currency = self._currency

        if self.ids.price_oxygen.text != '':
            dbedit_pricing.update_pricelist(name, 'o2',float(self.ids.price_oxygen.text))

        if self.ids.price_helium.text != '':
            dbedit_pricing.update_pricelist(name, 'he', float(self.ids.price_helium.text))
             
        if self.ids.price_service_fee.text != '':
            dbedit_pricing.update_pricelist(name,'service', int(self.ids.price_service_fee.text))
            
        if self.ids.price_tank_fee.text != '':
            dbedit_pricing.update_pricelist(name, 'tank', int(self.ids.price_tank_fee.text))
            
        if self._currency == None:
            self._currency = 'SEK'

        dbedit_pricing.update_pricelist(name, 'currency', self._currency)
            
    
        self.ids.price_oxygen.text = ''
        self.ids.price_air.text = ''
        self.ids.price_helium.text = ''
        self.ids.price_service_fee.text = ''
        self.ids.price_tank_fee.text = ''



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

    def change_values(self, fill_recipe, newoxygen,newhelium,newpressure,oldoxygen,oldhelium,oldpressure):
        self.ids.fill.text = fill_recipe
        self.ids.newo2.text = newoxygen 
        self.ids.oldo2.text = oldoxygen 
        self.ids.oldhe.text = oldhelium
        self.ids.newhe.text = newhelium 
        self.ids.oldpressure.text = oldpressure 
        self.ids.newpressure.text = newpressure

    def reset_values(self):

        pass
        



GUI = Builder.load_file('main.kv')
class MainApp(App):
    def build(self):
        return GUI
    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name
        



MainApp().run()