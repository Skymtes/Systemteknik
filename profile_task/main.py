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

# Dont remove these
import sys
import os
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('C:/Users/A11M1/Desktop/code/Systemteknik/backend/algorithm')
from backend.algorithm import blending
from backend import db_connect
from backend import dbedit_customer
from backend import dbedit_pricing
from backend import dbedit_rent
from backend import dbedit_scuba

exists = []

class HomeScreen(Screen):
    old_pressure = ObjectProperty(None)
    old_he = ObjectProperty(None)
    old_otwo = ObjectProperty(None)

    new_otwo = ObjectProperty(None)
    new_he = ObjectProperty(None)
    new_pressure = ObjectProperty(None)

    def btn(self):
        a = blending.Blend(float(self.new_otwo.text), float(self.new_he.text), float(self.new_pressure.text), float(self.old_otwo.text), float(self.old_he.text), float(self.old_pressure.text))
        self.manager.get_screen('more_info_screen').change_values(a)
        self.ids.old_pressure.text = ' '
        self.ids.old_he.text = ' '
        self.ids.old_otwo.text = ' '
        self.ids.new_otwo.text = ' '
        self.ids.new_he.text = ' '
        self.ids.new_pressure.text = ' '

  
class SettingsScreen(Screen):
    def button(self):
        pass


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
            name = profile[1].split(' ')
            self.button = Button(text=f'{name[1].upper()} , {name[0].upper()}',
                                 on_press= self.Press_auth)
            if self.button.text not in exists:
                self.ids.box.add_widget(self.button)
                exists.append(self.button.text)
            else:
                pass
    def Press_auth(self,instance):
        name = instance.text.lower().split(',')
        name = name[1].strip() + ' ' + name[0].strip()     
        self.button_press(name)
    def button_press(self,name):
       id = dbedit_customer.find_id(name.lower())
       customer = dbedit_customer.select_customer()
       for profile in customer:
            if profile[0] == id:
                self.manager.get_screen('profile_info_screen').insert_info(profile[1],profile[2],profile[3],profile[4],profile[5],profile[6])
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
        self.ids['gas_type'].text = "Gas Type: " + gas_type
        self.ids['date'].text = "Date: " + str(date)
        if not note:
            pass
        else:
            self.ids['note'].text = "Note: " + note

class TableScreen(Screen):
    pass 


class ImageButton(ButtonBehavior, Image):
    pass


class ProfileScreen(Screen):
    def on_reserved_press(self):
        self.manager.get_screen('reserved_profile_screen').add_button() 
class MoreInfoScreen(Screen):
    def change_values(self, fill_recipe):
        self.ids.fill.text = fill_recipe
        
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
