#kivy imports
from turtle import color
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior, Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from datetime import date

# kivyMD imports
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
#other imports
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from backend.algorithm import blending, blendingUtilities
from backend import dbedit_customer, dbedit_pricing
from functools import partial

class HomeScreen(Screen):
    old_pressure = ObjectProperty(None)
    old_he = ObjectProperty(None)
    old_otwo = ObjectProperty(None)

    new_otwo = ObjectProperty(None)
    new_he = ObjectProperty(None)
    new_pressure = ObjectProperty(None)

    def btn(self): # Calculate button in HomeScreen/BlendScreen
        
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

        if self.ids.tank_capacity.text == 'Capacity':
            self.ids.tank_capacity.text = '0'






        if self.ids.tank_capacity.text == '2x6':
            self.ids.tank_capacity.text = '12'
        
        if self.ids.tank_capacity.text == '2x7':
            self.ids.tank_capacity.text = '14'
        
        if self.ids.tank_capacity.text == '2x10':
            self.ids.tank_capacity.text = '20'
        
        if self.ids.tank_capacity.text == '2x12':
            self.ids.tank_capacity.text = '24'
        
        newBlend = blending.Blend( (float(self.new_otwo.text)) / 100, (float(self.new_he.text)) / 100, float(self.new_pressure.text), (float(self.old_otwo.text)) / 100, (float(self.old_he.text)) / 100, float(self.old_pressure.text)) # Values should be enterd Percentage / Pressure . 
        self.manager.get_screen('more_info_screen').BlendResult(newBlend, self.new_otwo.text, self.new_he.text, self.new_pressure.text, self.old_otwo.text, self.old_he.text, self.old_pressure.text)
        self.manager.get_screen('more_info_screen').GetPrice(int(self.ids.tank_capacity.text), newBlend)
        self.manager.get_screen('more_info_screen').min_max(blendingUtilities.MaxDepth(float(self.new_otwo.text)/100),blendingUtilities.MinDepth(float(self.new_otwo.text)/100))

    def on_reserved_press(self):
        self.manager.get_screen('reserved_profile_screen').add_button()

class SettingsScreen(Screen):

    _currency = None

    def on_pre_enter(self, *args): # Gets prices from database as soon as page switches to settings, Fills in values if database is empty

        if str(dbedit_pricing.GetOxygen()) == 'None':

            self.ids.price_oxygen.text = '0'

        else:

            self.ids.price_oxygen.text = str(dbedit_pricing.GetOxygen())

        if str(dbedit_pricing.GetHelium()) == 'None':

            self.ids.price_helium.text = '0'

        else:

            self.ids.price_helium.text = str(dbedit_pricing.GetHelium())

        if str(dbedit_pricing.GetAir()) == 'None':

            self.ids.price_air.text = '0'

        else:

            self.ids.price_air.text = str(dbedit_pricing.GetAir())

        if str(dbedit_pricing.fetch_tank_fee()) == 'None':

            self.ids.price_tank_fee.text = '0'

        else:

            self.ids.price_tank_fee.text = str(dbedit_pricing.fetch_tank_fee())

        if str(dbedit_pricing.GetServiceFee()) == 'None':

            self.ids.price_service_fee.text = '0'

        else:

            self.ids.price_service_fee.text = str(dbedit_pricing.GetServiceFee())

        if str(dbedit_pricing.fetch_currency()) == 'None':

            self.ids.currency.text = 'SEK'

        else:

            self.ids.currency.text = str(dbedit_pricing.fetch_currency())

        return super().on_pre_enter(*args)

    def button(self): # Needed for back-button

        pass

    def confirm(self): # Confirm button in settings

        if self.ids.price_oxygen.text == '':
            self.ids.price_oxygen.text = '0'

        if self.ids.price_helium.text == '':
            self.ids.price_helium.text = '0'

        if self.ids.price_air.text == '':
            self.ids.price_air.text = '0'

        if self.ids.price_tank_fee.text == '':
            self.ids.price_tank_fee.text = '0'

        if self.ids.price_service_fee.text == '':
            self.ids.price_service_fee.text = '0'

        dbedit_pricing.update_pricelist("UDT", 'o2',float(self.ids.price_oxygen.text))    
        dbedit_pricing.update_pricelist("UDT", 'air',float(self.ids.price_air.text))
        dbedit_pricing.update_pricelist("UDT", 'he', float(self.ids.price_helium.text))
        dbedit_pricing.update_pricelist("UDT",'service', int(self.ids.price_service_fee.text))
        dbedit_pricing.update_pricelist("UDT", 'tank', int(self.ids.price_tank_fee.text))
        dbedit_pricing.update_pricelist("UDT", 'currency', self.ids.currency.text)

class SelectCustomerScreen(Screen):
    def customers_view(self):
        self.ids.box_layout.clear_widgets()
        customer = dbedit_customer.select_customer()
        for profile in customer:
            self.label = Label(text=f'{profile[1]}', color=(0,0,0,1),pos_hint={'center_x':0.5, 'center_y':0.9})
            self.ids.box_layout.add_widget(self.label)
            self.active = CheckBox(active = False, pos_hint={'center_x':0.5, 'center_y':0.9})
            self.ids.box_layout.add_widget(self.active)
            self.active.bind(active=self.on_checkbox_active)
            #self.active.bind(on_release=self.on_checkbox_release)
    def on_checkbox_active(self, checkbox, value):
        if value:
            self.manager.get_screen('profile_info_screen').add_price_mix(price_currency)
    # def on_checkbox_release(self, checkbox):
    #     if checkbox.active:
    #         self.ids.box_layout.add_widget(self.label)
    #         self.ids.box_layout.add_widget(self.active)
    #     else:
    #         self.ids.box_layout.remove_widget(self.label)
    #         self.ids.box_layout.remove_widget(self.active)


    
class AddProfileScreen(Screen,MDApp):  
    def add_profile(self,name,number,email,spinner_type,note,set_date):
        dbedit_customer.create_customer(name.lower(),number,email,spinner_type,set_date)
        if note:
            id = dbedit_customer.find_id(name)
            dbedit_customer.create_customer_note(id,note)
        else:
            pass
    def on_reserved_press(self):
        self.manager.get_screen('reserved_profile_screen').add_button()
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
    def validate_email(self,email):
        if email.count('@') == 1 and email.count('.') == 1:
            print("valid email")
        else:
            print("invalid email")
            


class ReservedProfileScreen(Screen,Widget):
    def add_button(self):
        self.ids.box.clear_widgets()
        customer = dbedit_customer.select_customer()
        for profile in customer:
            self.button = Button(text=f'{profile[1]}',
                                 on_press= self.Press_auth)
            self.ids.box.add_widget(self.button)
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
    price = StringProperty('')
    mix = StringProperty('')
    dialog = None
    def insert_info(self,name,number,email,gas_type,note,date):
        self.ids['name'].text = "Name: " + name
        self.ids['number'].text = "Number: " + str(number)
        self.ids['email'].text = "Email: " + email
        self.ids['gas_type'].text = "Certificate: " + gas_type
        if str(date) == "Date":
            self.ids['date'].text = "Date: "
        else:
            self.ids['date'].text = "Date: " + str(date)
        if note:
            self.ids['note'].text = "Note: " + note
        else:
            self.ids['note'].text = "Note: "
    def alert_remove_profile(self,name_2):
        name = name_2.split(':')[1].strip().lower()
        id = dbedit_customer.find_id(name)
        Button_callback = partial(self.delete_profile,id)
        if not self.dialog:
            self.dialog = MDDialog(title=("Delete Profile:  " + name),
                                   type="custom",
                                   content_cls=Label(text="Are you sure you want to delete this profile?",color=(0,0,0,1)),
                                   buttons=[
                                       MDFlatButton(text="Cancel",on_release=self.cancel_remove_profile),
                                       MDRectangleFlatButton(text="Delete", on_release=Button_callback)
                                   ])
        self.dialog.open()
    def delete_profile(self,id,instance):
        dbedit_customer.remove_customer(id)
        self.manager.get_screen('reserved_profile_screen').add_button()
        self.dialog.dismiss()
        self.dialog = None
    def cancel_remove_profile(self,instance):
        self.dialog.dismiss()
        self.dialog = None
    def add_price_mix(self,price):
        self.ids['price'].text = "Price: " + str(price)
        #self.ids['mix'].text = "Mix: " + str(mix)

class ProfileScreen(Screen):
    def on_reserved_press(self):
        self.manager.get_screen('reserved_profile_screen').add_button()

class MoreInfoScreen(Screen):

    def BlendResult(self, fill_recipe, newoxygen, newhelium, newpressure, oldoxygen, oldhelium, oldpressure):

        if isinstance(fill_recipe, str):
            
            self.ids.fill.text = fill_recipe
        
        else:

            if fill_recipe[0] < 0 or fill_recipe[1] < 0 or fill_recipe[2] < 0:
                
                if -fill_recipe[0] + -fill_recipe[1] + -fill_recipe[2] == float(oldpressure):
                    
                    self.ids.fill.text = "Please lower the old tank to 0.0 Bar."
                
                else:

                    output = round(-fill_recipe[0] + -fill_recipe[1] + -fill_recipe[2] - 0.1, 1)

                    if output < 0:

                        self.ids.fill.text = "Please lower the old tank to 0.0 Bar."

                    else:
                    
                        self.ids.fill.text = f"Please lower the old tank to {output} Bar."
            
            elif str(fill_recipe[0]) == "-0.0":

                self.ids.fill.text = "Please lower the old tank to 0.0 Bar."

            else:
                
                self.ids.fill.text = f"Please fill the tank with\n{fill_recipe[0]} Bar Oxygen, (To {float(oldpressure) + fill_recipe[0]} Bar),\n{fill_recipe[1]} Bar Helium, (To {float(oldpressure) + fill_recipe[0] + fill_recipe[1]} Bar),\n{fill_recipe[2]} Bar Air, (To {float(oldpressure) + fill_recipe[0] + fill_recipe[1] + fill_recipe[2]} Bar)."

        self.ids.newo2.text = newoxygen 
        self.ids.oldo2.text = oldoxygen 
        self.ids.oldhe.text = oldhelium
        self.ids.newhe.text = newhelium 
        self.ids.oldpressure.text = oldpressure 
        self.ids.newpressure.text = newpressure

    def min_max(self, max,min): #function to present max/min depth
       self.ids.max_depth.text = (str(max) + 'm')
       self.ids.min_depth.text= (str(min) + 'm')


    def reset_values(self):
        pass

    def GetPrice(self, capacity, fill:list):

        if str(dbedit_pricing.GetOxygen()) == 'None':

            dbedit_pricing.update_pricelist("UDT", 'o2', '0')

        if str(dbedit_pricing.GetHelium()) == 'None':

            dbedit_pricing.update_pricelist("UDT", 'he', '0')

        if str(dbedit_pricing.GetAir()) == 'None':

            dbedit_pricing.update_pricelist("UDT", 'air', '0')

        if str(dbedit_pricing.fetch_tank_fee()) == 'None':

            dbedit_pricing.update_pricelist("UDT", 'tank', '0')

        if str(dbedit_pricing.GetServiceFee()) == 'None':

            dbedit_pricing.update_pricelist("UDT", 'service', '0')

        if str(dbedit_pricing.fetch_currency()) == 'None':

            dbedit_pricing.update_pricelist("UDT", 'currency', 'SEK')

        price = dbedit_pricing.calculate_tank_price(capacity, fill)
        currency = dbedit_pricing.fetch_currency()

        global price_currency
        price_currency = price

        if price < 0: # Shouldn't be able to recieve money

            price = 0

        self.ids.tank_price.text = f"{'Total: ' + str(price) + ' ' + currency}\nOxygen: {str(round(fill[0] * capacity * dbedit_pricing.GetOxygen(), 2)) + ' ' + currency}\nHelium: {str(round(fill[1] * capacity * dbedit_pricing.GetHelium(), 2)) + ' ' + currency}\nAir: {str(round(fill[2] * capacity * dbedit_pricing.GetAir(), 2)) + ' ' + currency}"

    def customer_select(self):
        self.manager.get_screen('select_customer_screen').customers_view()
        
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
        


#Window.size = (360, 740)
MainApp().run()
