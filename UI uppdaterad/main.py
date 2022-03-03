from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior



class HomeScreen(Screen):
    pass
class SettingsScreen(Screen):
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