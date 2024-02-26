from kivy.uix.boxlayout import BoxLayout
from tools.Utils import *

from kivymd.app import MDApp

class MainControllerLayout(BoxLayout):
    
    app=MDApp.get_running_app()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        pass
        
