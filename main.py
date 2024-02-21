import tools.i18n as i18n
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from functools import partial
import tools.customWidgets as customWidgets
import json
import tools.Globals as Globals
from kivy.lang import Builder
from kivy.metrics import dp

##Localization
translator = i18n.Translator('tools/localization/')

    

class ZequentMavLinkApp(MDApp):

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
                Builder.load_file(os.path.join(currDirName, filename)) 

    def get_welcome_text(self):
        return translator.translate('welcome')
    
    def callback(self,x):
        print(x)
        
    ##Change Screen
    def changeScreen(self,*args):
        self.root.ids.sm.current = args[0]

    def open_language_dropdown(self, item,sm):
        menu_items = self.getLanguageDropDownItems(sm)
        MDDropdownMenu(caller=item, items=menu_items).open()

    def getLanguageDropDownItems(self,sm):
        from os import walk

        availableLanguages = []
        for (dirpath, dirnames, filenames) in walk('tools/localization/'):
            filenames = filenames
            break

        for filename in filenames:
            filename = filename.split('.json')[0]
            currLanguageDropDownItem = {
                "text": filename,
                "font_size": self.fontSizes['primary'],
                "on_release": lambda language=filename: self.setLanguage(language,sm),
            }
            availableLanguages.append(currLanguageDropDownItem)
        
        return availableLanguages
    
    ###TODO: Test refresh
    def changeLanguageOnStart(self, topBar):
        menu_items = self.getDropDownItemsLanguage()
        mdDropDown = MDDropdownMenu()
        mdDropDown.caller=topBar
        mdDropDown.items=menu_items
        mdDropDown.pos_hint= {'center_x':.5,'center_y':.5}
        mdDropDown.open()
    
    def setLanguage(self, language,sm):
        ###TODO CHANGE SCREEN
        from kivy.uix.screenmanager import ScreenManager, Screen
        translator.set_locale(language)
        self.saveInSettings(language)
        updateScreen = sm.get_screen(sm.current)
        updateScreen.name = sm.current
        sm.add_widget(updateScreen)
        sm.remove_widget(sm.get_screen(sm.current))
        sm.current = updateScreen.name
        
    
    def saveInSettings(self, language):
        with open(Globals.settingsFile) as infile:
            data = json.load(infile)
        data["lastUsedLanguage"] = language
        with open(Globals.settingsFile, 'w') as outfile:
            json.dump(data, outfile)
    
    
    def menu_callback(self, text_item):
        print(str(text_item))
    ######ZequentConnectLayout End#######
        
if __name__ == '__main__':
    ZequentMavLinkApp().run()