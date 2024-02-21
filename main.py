import tools.i18n as i18n
from kivymd.app import MDApp
from kivy.clock import Clock
from functools import partial
import tools.customWidgets as customWidgets
import tools.Globals as Globals
from kivy.lang import Builder
from kivy.metrics import dp
from tools.py_files.layouts.zequentrootlayout import *
from tools.py_files.screens.connectionscreen import *


class ZequentMavLinkApp(MDApp):

    translator = i18n.Translator('tools/localization/')

    customColors = {
        #Gold
        "first": [0.78,0.56,0.05,1],
        #Gold-secondary
        "second": [0.78,0.56,0.05,0.5],
        #Black
        "black": [0,0,0,0.9],
        #Jewel-primary
        "fourth": [0.00392, 0.14117, 0.3607],
        "success": [0,1,0,1],
        "failure": [1,0,0,1]
    }

    fontSizes = {
        #Big
        "primary": dp(40),

        #Medium
        "secondary": dp(30),

        #small
        "tertiary": dp(20)
    }

    toolBarTitle = "MavLink"

    connected = False

    def __init__(self, **kwargs):
        self.title = "My Material Application"
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Dark"
        self.importPY_FILES()
        self.importKV_FILES()

    def build(self):
        pass

    ###IMPORT ALL PY_FILES
    def importPY_FILES(self):
        import glob
        import importlib.util
        for filename in glob.iglob('tools/py_files/' + '**/**.py', recursive=True):
            filename = filename.replace("/",".")
            filename = filename[:-3]
            if "__pycache__" not in filename:
                importlib.import_module(filename)


    ###IMPORT ALL KV_FILES
    def importKV_FILES(self):
        import os
        for currDirName, dirnames, filenames in os.walk('./tools/kv_files'):
            for filename in filenames:
                print(os.path.join(currDirName, filename))
                Builder.load_file(os.path.join(currDirName, filename)) 
    
    
     ##Change Screen
    def changeScreen(self,*args):
        self.root.ids.sm.current = args[0]
        
if __name__ == '__main__':
    ZequentMavLinkApp().run()