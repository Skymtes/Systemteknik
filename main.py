from lib2to3.pgen2 import driver
from turtle import color
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

class ReservedProfileScreen(Screen):
    pass
class AddProfileScreen(Screen): 
    txt_air = StringProperty()
    def spinner_clicked_type(self,value):
        print("value",value) 
    #def add_profile(self,name)

class ProfileInfoScreen(Screen):
    pass

class TableScreen(Screen):
    pass 


class ImageButton(ButtonBehavior, Image):
    pass


class ProfileScreen(Screen):
    pass 
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

