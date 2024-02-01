import i18n
import kivy
from kivymd.app import MDApp


translator = i18n.Translator('localization/')
translator.set_locale('de')

class ZequentMavLinkApp(MDApp):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    
    def callback(self,x):
        print(x)

    def get_welcome_text(self):
        return translator.translate('welcome')



if __name__ == '__main__':
    ZequentMavLinkApp().run()