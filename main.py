#kivy imports
from turtle import color, onclick
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior, Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.checkbox import CheckBox
from datetime import date
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

#other imports
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from backend.algorithm import blending, blendingUtilities
from backend import dbedit_customer, dbedit_pricing, dbedit_rent
from functools import partial
from numbers import Number

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
        remember_capacity = self.ids.tank_capacity.text
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

        self.ids.tank_capacity.text = remember_capacity

    def on_reserved_press(self):
        self.manager.get_screen('reserved_profile_screen').add_button()

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
        global blend_result
        blend_result = f"{fill_recipe[0]} Bar Oxygen, (To {float(oldpressure) + fill_recipe[0]} Bar),\n{fill_recipe[1]} Bar Helium, (To {float(oldpressure) + fill_recipe[0] + fill_recipe[1]} Bar),\n{fill_recipe[2]} Bar Air, (To {float(oldpressure) + fill_recipe[0] + fill_recipe[1] + fill_recipe[2]} Bar)."
    def testone(self):
        
        if self.ids.old_pressure.text != '' and self.ids.old_he.text != '' and self.ids.old_otwo.text != '' and self.ids.new_otwo.text != '' and self.ids.new_he.text != '' and self.ids.new_pressure.text != '' and self.ids.tank_capacity.text != 'Capacity':
            
            if self.ids.tank_capacity.text == '2x6':
                self.ids.tank_capacity.text = '12'
            
            if self.ids.tank_capacity.text == '2x7':
                self.ids.tank_capacity.text = '14'
            
            if self.ids.tank_capacity.text == '2x10':
                self.ids.tank_capacity.text = '20'
            
            if self.ids.tank_capacity.text == '2x12':
                self.ids.tank_capacity.text = '24'
            newBlend = blending.Blend( (float(self.new_otwo.text)) / 100, (float(self.new_he.text)) / 100, float(self.new_pressure.text), (float(self.old_otwo.text)) / 100, (float(self.old_he.text)) / 100, float(self.old_pressure.text)) # Values should be enterd Percentage / Pressure . 
            self.BlendResult(newBlend, self.new_otwo.text, self.new_he.text, self.new_pressure.text, self.old_otwo.text, self.old_he.text, self.old_pressure.text)
            self.GetPrice(float(self.ids.tank_capacity.text), newBlend)
            self.min_max(blendingUtilities.MaxDepth(float(self.new_otwo.text)/100),blendingUtilities.MinDepth(float(self.new_otwo.text)/100))

        
    def min_max(self, max,min): #function to present max/min depth
        self.ids.max_depth.text = ( '(Tx)' + ' ' + 'Max Depth' + ' ' + str(max) + 'm')
        self.ids.min_depth.text = ('(Tx)' + ' ' + 'Min Depth' + ' ' + str(min) + 'm')
        
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
        self.ids.select_customer_grid.clear_widgets()
        customer = dbedit_customer.select_customer()
        for profile in customer:
            self.button = Button(text=f'{profile[1]}', on_press= self.add_pric_mix)
            self.ids.select_customer_grid.add_widget(self.button)
    def add_pric_mix(self,instance):
        name = instance.text.lower()
        instance.background_color = (0,1,0,1)
        id = dbedit_customer.find_id(name.lower())
        customer = dbedit_customer.select_customer()
        for profile in customer:
            if profile[0] == id:
                dbedit_rent.create_rented(blend_result,price_currency,id)
                break

    def change_background(self, instance):
        instance.background_color = (1,1,1,1)

    
class AddProfileScreen(Screen):
    def add_profile(self,name,number,email,spinner_type,note,set_date):
        dbedit_customer.create_customer(name.lower(),number,email,spinner_type,set_date)
        if note:
            id = dbedit_customer.find_id(name)
            dbedit_customer.create_customer_note(id,note)
        else:
            pass
    def on_reserved_press(self):
        self.manager.get_screen('reserved_profile_screen').add_button()
    def reset_info(self):
        self.ids.name.text = ''
        self.ids.number.text = ''
        self.ids.email.text = ''
        self.ids.note.text = ''
        self.ids.spinner_type.text = 'Air'
            

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
                self.manager.get_screen('profile_info_screen').insert_info(profile[0],profile[1],profile[2],profile[3],profile[4],profile[6],profile[5])
                self.manager.current= 'profile_info_screen'
                break
    def search_customer(self):
        self.ids.box.clear_widgets()
        customer = dbedit_customer.select_customer()
        for profile in customer:
            if self.ids.search_input.text.isdigit():
                if profile[0] == int(self.ids.search_input.text):
                    self.button = Button(text=f'{profile[1]}',
                                        on_press= self.Press_auth)
                    self.ids.box.add_widget(self.button)
            else:
                if profile[1].lower().startswith(self.ids.search_input.text.lower()):
                    self.button = Button(text=f'{profile[1]}',
                                        on_press= self.Press_auth)
                    self.ids.box.add_widget(self.button)

class ProfileInfoScreen(Screen,Widget):
    name = StringProperty('')
    number = StringProperty('')
    email = StringProperty('')
    gas_type = StringProperty('')
    note = StringProperty('')
    date = StringProperty('')
    price = StringProperty('')
    mix = StringProperty('')
    def insert_info(self,id,name,number,email,gas_type,note,date):
        self.ids['name'].text = name
        self.ids['number'].text = str(number)
        self.ids['email'].text = email
        self.ids['gas_type'].text = gas_type
        if str(date) == "Date":
            self.ids['date'].text = ""
        else:
            self.ids['date'].text = str(date)
        if note:
            self.ids['note'].text = note 
        else:
            self.ids['note'].text = ""
        rented_tank = dbedit_rent.get_rented(id)
        if rented_tank:
            for key in rented_tank:
                if key == id:
                    self.ids.gas_info_box.clear_widgets()
                    tank = rented_tank[key]
                    nums = [num for num in tank if isinstance(num, Number)]
                    str_mix = [_str for _str in tank if isinstance(_str, str)]
                    self.ids['price'].text = str(sum(nums))
                    for idx,mix in enumerate(str_mix):
                        self.lbl_mix = Label(text=mix, color=(0,1,0,1))
                        self.lbl_price = Label(text=str(nums[idx]), color=(0,1,0,1))
                        self.ids.gas_info_box.add_widget(self.lbl_mix)
                        self.ids.gas_info_box.add_widget(self.lbl_price)
                        self.ids.gas_info_box.add_widget(Label(text='\n\n\n\n\n\n\n\n\n\n\n\n'))


                #mix_text = ''.join(f'({mix} \n____________\n {nums[idx]} \n ' for idx,mix in enumerate(str_mix))
                #self.ids['mix'].text = mix_text
        else:
            self.ids['price'].text = ""
            self.ids.gas_info_box.clear_widgets()
    def alert_remove_profile(self,name):
        id = dbedit_customer.find_id(name)
        button_callback = partial(self.delete_profile,id) 
        self.box=FloatLayout() 
        self.lab=(Label(text="Are you sure you want delet this profile",font_size=15, 
        	size_hint=(None,None),pos_hint={'x':.35,'y':.5})) 
        self.box.add_widget(self.lab) 
        self.but=(Button(text="Yes",size_hint=(None,None), 
        	width=200,height=50,pos_hint={'x':.25,'y':0},on_press=button_callback)) 
        self.box.add_widget(self.but) 
        self.main_pop = Popup(title=name,content=self.box, 
        	size_hint=(None,None),size=(450,200),auto_dismiss=True,title_size=25)  
        self.but.bind(on_press=self.main_pop.dismiss) 
        self.main_pop.open()
    def delete_profile(self,id,instance):
        dbedit_customer.remove_customer(id)
        self.manager.get_screen('reserved_profile_screen').add_button()
    def add_price_mix(self,price):
        self.ids['price'].text = str(price)
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
        if price < 0: # Shouldn't be able to recieve money
            price = 0
        price_currency = f"{price} {currency}"
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


MainApp().run()
