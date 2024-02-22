from kivymd.uix.toolbar.toolbar import MDTopAppBar
import tools.i18n as i18n
from kivymd.uix.menu import MDDropdownMenu
import json
import tools.Globals as Globals
from kivymd.app import MDApp

class ZequentAppBar(MDTopAppBar):
    #Localization
    translator = i18n.Translator('tools/localization/')
    app= MDApp.get_running_app()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def open_language_dropdown(self, item):
        menu_items = self.getLanguageDropDownItems()
        MDDropdownMenu(caller=item, items=menu_items).open()

    def getLanguageDropDownItems(self):
        from os import walk

        availableLanguages = []
        for (dirpath, dirnames, filenames) in walk('tools/localization/'):
            filenames = filenames
            break

        for filename in filenames:
            filename = filename.split('.json')[0]
            currLanguageDropDownItem = {
                "text": filename,
                "font_size": self.app.fontSizes['primary'],
                "on_release": lambda language=filename: self.setLanguage(language),
            }
            availableLanguages.append(currLanguageDropDownItem)
        
        return availableLanguages
    
    def changeLanguageOnStart(self, topBar):
        menu_items = self.getDropDownItemsLanguage()
        mdDropDown = MDDropdownMenu()
        mdDropDown.caller=topBar
        mdDropDown.items=menu_items
        mdDropDown.pos_hint= {'center_x':.5,'center_y':.5}
        mdDropDown.open()
    
    def setLanguage(self, language):
        ###TODO CHANGE SCREEN
        from kivy.uix.screenmanager import ScreenManager, Screen
        self.translator.set_locale(language)
        self.saveInSettings(language)
        
    def saveInSettings(self, language):
        with open(Globals.settingsFile) as infile:
            data = json.load(infile)
        data["lastUsedLanguage"] = language
        with open(Globals.settingsFile, 'w') as outfile:
            json.dump(data, outfile)
    
    def callback(self,x):
        print(x)
    
    def menu_callback(self, text_item):
        print(str(text_item))