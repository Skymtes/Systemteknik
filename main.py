from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.properties import ObjectProperty
from kivy.uix.checkbox import CheckBox
from Algorithm import Blending


class HomeScreen(Screen):
    old_pressure = ObjectProperty(None)
    old_he = ObjectProperty(None)
    old_otwo = ObjectProperty(None)

    new_otwo = ObjectProperty(None)
    new_he = ObjectProperty(None)
    new_pressure = ObjectProperty(None)




    def btn(self):
        
        a = Blending.Blend(float(self.new_otwo.text), float(self.new_he.text), float(self.new_pressure.text), float(self.old_otwo.text), float(self.old_he.text), float(self.old_pressure.text))
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




class AddProfileScreen(Screen):
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