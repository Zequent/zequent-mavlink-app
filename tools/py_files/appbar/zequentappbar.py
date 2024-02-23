from kivymd.uix.toolbar.toolbar import MDTopAppBar
import tools.i18n as i18n
from kivymd.uix.menu import MDDropdownMenu
import json
from tools.Globals import *
from kivymd.app import MDApp
from tools.py_files.widgets.zequentbutton import *
from functools import partial
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

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
        self.app= MDApp.get_running_app()
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
                "on_release": lambda language=filename: self.show_alert_dialog(language),
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
    


    def setLanguage(self, *args):
        self.translator.set_locale(args[0])
        self.saveInSettings(args[0])
    
    def show_alert_dialog(self, language):
        cancelButton = MDFlatButton()
        cancelButton.text = self.translator.translate("cancel")
        submitButton = MDFlatButton()
        submitButton.text=self.translator.translate("submit")
        submitButton.bind(on_press=partial(self.setLanguage,language))
        dialog = MDDialog(
                buttons=[
                    cancelButton,
                    submitButton
                ]
            )
        dialog.text = self.translator.translate('restart_text')

        dialog.open()



    def saveInSettings(self, language):
        with open(Globals.getSettingsFile()) as infile:
            data = json.load(infile)
        data["lastUsedLanguage"] = language
        with open(Globals.getSettingsFile(), 'w') as outfile:
            json.dump(data, outfile)
            self.app.stop()
    
    def callback(self,x):
        print(x)
    
    def menu_callback(self, text_item):
        print(str(text_item))