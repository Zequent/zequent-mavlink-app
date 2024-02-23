from kivy.uix.boxlayout import BoxLayout
import tools.i18n as i18n
from kivymd.app import MDApp
from tools.Globals import *

class ZequentRootLayout(BoxLayout):
    translator = i18n.Translator(Globals.getTranslatorFolder())
    app= MDApp.get_running_app()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def build(self):
        pass

   
    
   

    