from kivymd.uix.toolbar.toolbar import MDTopAppBar
import tools.i18n as i18n
from tools.py_files.widgets.zequentdropdownmenu import *
import json
from tools.Globals import *
from kivymd.app import MDApp
from tools.py_files.widgets.zequentbutton import *
from functools import partial
from tools.py_files.widgets.zequentdialog import *
from tools.py_files.widgets.zequentflatbutton import *

class ZequentAppBar(MDTopAppBar):
    translator = i18n.Translator(Globals.getTranslatorFolder())
    app=MDApp.get_running_app()
    submitDialog = None
    languageDropdown = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        pass
    
    def open_language_dropdown(self, item):
        self.languageDropdown = ZequentDropDownMenu(caller=item, items=self.getLanguageDropDownItems())
        self.languageDropdown.open()

    def getLanguageDropDownItems(self):
        self.app= MDApp.get_running_app()
        from os import walk

        availableLanguages = []
        for (dirpath, dirnames, filenames) in walk(Globals.getTranslatorFolder()):
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
    
    def show_alert_dialog(self, language):
        cancelButton = MDFlatButton()
        cancelButton.text = self.translator.translate("cancel")
        cancelButton.bind(on_press=self.hide_alert_dialog) 
        submitButton = MDFlatButton()
        submitButton.text=self.translator.translate("submit")
        submitButton.bind(on_press=partial(self.setLanguage,language))
        self.submitDialog = ZequentDialog(
                buttons=[
                    cancelButton,
                    submitButton
                ]
            )
        self.submitDialog.text = self.translator.translate('restart_text')
        self.submitDialog.open()

    def setLanguage(self, *args):
        self.translator.set_locale(args[0])
        self.saveInSettings(args[0])
    

    def saveInSettings(self, language):
        with open(Globals.getSettingsFile()) as infile:
            data = json.load(infile)
        data["lastUsedLanguage"] = language
        with open(Globals.getSettingsFile(), 'w') as outfile:
            json.dump(data, outfile)
            self.app.stop()

    def hide_alert_dialog(self, instance):
        self.languageDropdown.dismiss()
        self.submitDialog.dismiss()