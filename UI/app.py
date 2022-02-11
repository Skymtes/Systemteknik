from tkinter import ON
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import StringProperty

kv = Builder.load_file("my.kv")



class StartWindow(Screen):

    def submit1(self):
        sm.current = 'first'
        
    def submit2(self):
        sm.current = 'second'

    def submit3(self):
        sm.current = 'third'

    def submit4(self):
        sm.current = 'fourth'    

    def submit5(self):
        sm.current = 'fifth'

    def submit6(self):
        sm.current = 'sixth'




class FirstOption(Screen):
    otwo = ObjectProperty(None)
    def submit(self):
        sm.current = 'start'
            



class SecondOption(Screen):
    def submit(self):
        sm.current = 'start'



class ThirdOption(Screen):
    def submit(self):
        sm.current = 'start'



class FourthOption(Screen):
    def submit(self):
        sm.current = 'start'


class FifthOption(Screen):
    otwo = ObjectProperty(None)
    ntwo = ObjectProperty(None)
    press = ObjectProperty(None)

    otwo1 = ObjectProperty(None)
    ntwo1 = ObjectProperty(None)
    press1 = ObjectProperty(None)
    

    def submit(self):
        sm.current = 'start'
       


class SixthOption(Screen):
    def submit(self):
        sm.current = 'start'


class WindowManager(ScreenManager):
    pass




sm = WindowManager()


screens = [StartWindow(name="start"), FirstOption(name='first'), SecondOption(name='second'), ThirdOption(name='third'), FourthOption(name='fourth'), FifthOption(name='fifth'), SixthOption(name='sixth')]
for screen in screens:
    sm.add_widget(screen)

sm.current = 'start'


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()