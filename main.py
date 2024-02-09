import tools.i18n as i18n
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import BooleanProperty
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock
from functools import partial
import tools.customWidgets as customWidgets




class ZequentMavLinkApp(MDApp):
    ##Localization
    translator = i18n.Translator('tools/localization/')
    translator.set_locale('de')

    toolBarTitle = "MavLink"
    ##Custom ColorPlaette
    colors = {
        "Black-primary": [0,0,0,0.9],
        "Gold-primary": [0.78,0.56,0.05,1],
        "Gold-secondary": [0.78,0.56,0.05,0.5],
        "Jewel-primary": [0.00392, 0.14117, 0.3607],
        "Success": [0,1,0,1],
        "Failure": [1,0,0,1],
    }

    #connection status variable of return value from API
    connected = False
    
    #Startpoint
    def build(self):
        self.theme_cls.theme_style = "Dark"

    ######Globals Start#######
    def get_welcome_text(self):
        return self.translator.translate('welcome')
    
    def callback(self,x):
        print(x)
    ######Globals End#######
        
    ##Start new Root Screen
    def setNewScreen(self,*args):
        self.root.clear_widgets()
        self.root.add_widget(args[0])

    ######ZequentRootLayout Start#######
    ##Connect to Vehicle
    def tryConnection(self,button, connectionType):
        ###TODO: Define connect function with api###
        import random
        randInt = random.randint(0,1)
        currStateLabel = self.root.ids.connection_status_label
        
        if connectionType.ids.rfc_button.disabled == False:
            print("RFC")
        elif connectionType.ids.lte_button.disabled == False:
            lteAddress=connectionType.ids.lte_address
            print("LTE adress:"+str(lteAddress.text))
        if randInt is 0:
            currStateLabel.text = self.translator.translate('failed_message')
            currStateLabel.color = self.colors["Failure"]
        else:
            button.disabled = True
            currStateLabel.text = self.translator.translate('success_message')
            currStateLabel.color = self.colors["Success"]
            Clock.schedule_once(partial(self.setNewScreen, customWidgets.MainControllerLayout()), 3)
    ######ZequentRootLayout End#######


    ######ZequentConnectLayout Start#######
    def getConnectionStatusText(self):
        return self.translator.translate('not_connected')
    
    def openDropDownSettings(self,topBar):
        menu_items = self.getDropDownItemsSettings()
        mdDropDown = MDDropdownMenu()
        mdDropDown.caller=topBar
        mdDropDown.items=menu_items
        mdDropDown.pos_hint= {'center_x':.5,'center_y':.5}
        mdDropDown.open()

    def getDropDownItemsSettings(self):
        ###TODO: DEFINE AVAILABLE FUNCTIONS###
        return [
            {
                "text": f"Item {i}",
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]

    def openDropDownLanguageSelection(self,topBar):
        menu_items = self.getDropDownItemsLanguage()
        mdDropDown = MDDropdownMenu()
        mdDropDown.caller=topBar
        mdDropDown.items=menu_items
        mdDropDown.pos_hint= {'center_x':.5,'center_y':.5}
        mdDropDown.open()

    def getDropDownItemsLanguage(self):
        ###TODO: DEFINE AVAILABLE FUNCTIONS###
        from os import walk

        availableLanguages = []
        for (dirpath, dirnames, filenames) in walk('tools/localization/'):
            filenames = filenames
            break

        for filename in filenames:
            filename = filename.split('.json')[0]
            currLanguageDropDownItem = {
                "text": filename,
                "on_release": lambda x=filename: self.setLanguage(x)
            }
            availableLanguages.append(currLanguageDropDownItem)
        
        return availableLanguages
    
    def setLanguage(self, language):
        self.translator.set_locale(language)
        self.setNewScreen(customWidgets.MainControllerLayout())
    

    def menu_callback(self, text_item):
        print(str(text_item))
    ######ZequentConnectLayout End#######
        
if __name__ == '__main__':
    ZequentMavLinkApp().run()