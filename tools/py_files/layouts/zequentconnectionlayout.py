from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import tools.i18n as i18n
from functools import partial
import tools.i18n as i18n

class ZequentConnectionLayout(BoxLayout):
    
    ##Localization
    translator = i18n.Translator('tools/localization/')

    connectionStatusText = translator.translate('not_connected')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def tryConnection(self,button, connectionType, currStateLabel, app):
            ###TODO: Define connect function with api###
            import random
            randInt = random.randint(0,1)
            if self.ids.rfc_button.disabled == False:
                print("RFC")
            elif self.ids.lte_button.disabled == False:
                lteAddress=self.ids.lte_address
                print("LTE adress:"+str(lteAddress.text))
            if randInt == 0:
                currStateLabel.text = self.translator.translate('failed_message')
                currStateLabel.color = app.customColors["failure"]
            else:
                button.disabled = True
                currStateLabel.text = self.translator.translate('success_message')
                currStateLabel.color = app.customColors["success"]
                Clock.schedule_once(partial(app.changeScreen, '__main_screen__'), 3)
                print("OK")