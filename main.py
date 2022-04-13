import kivy
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior, Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker

from datetime import date
import sys
import os
import sqlite3


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from backend.algorithm import blending
from backend import db_connect, dbedit_customer, dbedit_pricing, dbedit_rent, dbedit_scuba

exists = []


class HomeScreen(Screen):
    old_pressure = ObjectProperty(None)
    old_he = ObjectProperty(None)
    old_otwo = ObjectProperty(None)

    new_otwo = ObjectProperty(None)
    new_he = ObjectProperty(None)
    new_pressure = ObjectProperty(None)

    def btn(self):
        
        if self.ids.old_pressure.text == '':
            self.ids.old_pressure.text = '0'

        if self.ids.old_he.text == '':
            self.ids.old_he.text = '0'

        if self.ids.old_otwo.text == '':
            self.ids.old_otwo.text = '0'

        if self.ids.new_otwo.text == '':
            self.ids.new_otwo.text = '0'

        if self.ids.new_he.text == '':
            self.ids.new_he.text = '0'
            
        if self.ids.new_pressure.text == '':
            self.ids.new_pressure.text = '0'

        a = blending.Blend( (float(self.new_otwo.text))/100, (float(self.new_he.text))/100, float(self.new_pressure.text), (float(self.old_otwo.text))/100, (float(self.old_he.text))/100, float(self.old_pressure.text)) #Values should be enterd in Procents/Bar. 
        self.manager.get_screen('more_info_screen').change_values(a, self.new_otwo.text,self.new_he.text,self.new_pressure.text,self.old_otwo.text,self.old_he.text,self.old_pressure.text)
        self.manager.get_screen('more_info_screen').tank_price(int(self.new_pressure.text),[int(self.new_otwo.text),int(self.new_he.text),0.25])


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
            dbedit_pricing.update_pricelist("UDT", 'o2',float(self.ids.price_oxygen.text))

        if self.ids.price_oxygen.text != '':
            dbedit_pricing.update_pricelist("UDT", 'air',float(self.ids.price_air.text))

        if self.ids.price_helium.text != '':
            dbedit_pricing.update_pricelist("UDT", 'he', float(self.ids.price_helium.text))
             
        if self.ids.price_service_fee.text != '':
            dbedit_pricing.update_pricelist("UDT",'service', int(self.ids.price_service_fee.text))
            
        if self.ids.price_tank_fee.text != '':
            dbedit_pricing.update_pricelist("UDT", 'tank', int(self.ids.price_tank_fee.text))
            
        if self._currency == None:
            self._currency = 'SEK'

        dbedit_pricing.update_pricelist("UDT", 'currency', self._currency)
            
    
        #self.ids.price_oxygen.text = ''
        #self.ids.price_air.text = ''
        #self.ids.price_helium.text = ''
        #self.ids.price_service_fee.text = ''
        #self.ids.price_tank_fee.text = ''



class SelectCustomerScreen(Screen):
    pass
class AddProfileScreen(Screen,MDApp):  
    def add_profile(self,name,number,email,spinner_type,note,set_date):
        dbedit_customer.create_customer(name.lower(),number,email,spinner_type,set_date)
        if note:
            id = dbedit_customer.find_id(name)
            dbedit_customer.create_customer_note(id,note)
        else:
            pass
    def date_picker(self):
        todays_date = date.today()
        data_dialog = MDDatePicker(year=todays_date.year, month=todays_date.month, day=todays_date.day)
        data_dialog.bind(on_save= self.on_save, on_cancel=self.on_cancel)
        data_dialog.open()
    def on_save(self, instance,value,date_range):
        self.ids.date_label.text = str(value) 
    def on_cancel(self, instance,value):
        self.ids.date_label.text = 'you cancelled'    
    def reset_info(self):
        self.ids.name.text = ''
        self.ids.number.text = ''
        self.ids.email.text = ''
        self.ids.note.text = ''
        self.ids.spinner_type.text = 'Air'
        self.ids.date_label.text = 'Date'


class ReservedProfileScreen(Screen,Widget):
    def add_button(self,):
        customer = dbedit_customer.select_customer()
        for profile in customer:
            self.button = Button(text=f'{profile[1]}',
                                 on_press= self.Press_auth)
            if self.button.text not in exists:
                self.ids.box.add_widget(self.button)
                exists.append(self.button.text)
            else:
                pass
    def Press_auth(self,instance):
        name = instance.text.lower() 
        self.button_press(name)
    def button_press(self,name):
       id = dbedit_customer.find_id(name.lower())
       customer = dbedit_customer.select_customer()
       for profile in customer:
            if profile[0] == id:
                self.manager.get_screen('profile_info_screen').insert_info(profile[1],profile[2],profile[3],profile[4],profile[6],profile[5])
                self.manager.current= 'profile_info_screen'
                break

class ProfileInfoScreen(Screen,Widget):
    name = StringProperty('')
    number = StringProperty('')
    email = StringProperty('')
    gas_type = StringProperty('')
    note = StringProperty('')
    date = StringProperty('')
    def insert_info(self,name,number,email,gas_type,note,date):
        self.ids['name'].text = "Name: " + name
        self.ids['number'].text = "Number: " + str(number)
        self.ids['email'].text = "Email: " + email
        self.ids['gas_type'].text = "Certificate: " + gas_type
        if str(date) == "Date":
            self.ids['date'].text = "Date: "
        else:
            self.ids['date'].text = "Date: " + str(date)
        if not note:
            self.ids['note'].text = "Note: "
        else:
            self.ids['note'].text = "Note: " + note

class ProfileScreen(Screen):
    def on_reserved_press(self):
        self.manager.get_screen('reserved_profile_screen').add_button() 

class MoreInfoScreen(Screen):

    def change_values(self, fill_recipe, newoxygen,newhelium,newpressure,oldoxygen,oldhelium,oldpressure):
        if isinstance(fill_recipe, str):
            self.ids.fill.text = fill_recipe
        else:
            if fill_recipe[0] < 0 or fill_recipe[1] < 0 or fill_recipe[2] < 0:
                if -fill_recipe[0] + -fill_recipe[1] + -fill_recipe[2] == oldpressure:
                    self.ids.fill.text = "Please empty the old tank before filling"
                else:
                    self.ids.fill.text = f"Please lower the old tank to {-fill_recipe[0] + -fill_recipe[1] + -fill_recipe[2] - 0.1} Bar"
            else:
                self.ids.fill.text = f"Please fill with \n {fill_recipe[0]} Bar Oxygen \n {fill_recipe[1]} Bar Helium \n {fill_recipe[2]} Bar Air"

        self.ids.newo2.text = newoxygen 
        self.ids.oldo2.text = oldoxygen 
        self.ids.oldhe.text = oldhelium
        self.ids.newhe.text = newhelium 
        self.ids.oldpressure.text = oldpressure 
        self.ids.newpressure.text = newpressure

    def reset_values(self):
        pass

    def tank_price(self,capacity,fill:list):
        self.ids.tank_price.text = str(dbedit_pricing.calculate_tank_price(capacity,fill))
        
class TableScreen(Screen):
    pass 


class ImageButton(ButtonBehavior, Image):
    pass

GUI = Builder.load_file('main.kv')
class MainApp(App):
    def build(self):
        return GUI
    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name
        



MainApp().run()