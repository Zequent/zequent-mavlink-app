from kivy.uix.boxlayout import BoxLayout
import tools.i18n as i18n
from kivymd.app import MDApp

class ZequentRootLayout(BoxLayout):
    ##Localization
    translator = i18n.Translator('tools/localization/')
    app= MDApp.get_running_app()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("-----------------------------------")
        print("-----------------------------------")
        print("-----------------------------------")
        print("-----------------------------------")
        print("-----------------------------------")
        print("-----------------------------------")
        print("-----------------------------------")
        print("-----------------------------------")
        

    def build(self):
        pass

   
    
   

    