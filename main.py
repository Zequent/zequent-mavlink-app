import tools.i18n as i18n
from kivymd.app import MDApp

translator = i18n.Translator('tools/localization/')
translator.set_locale('de')



class ZequentMavLinkApp(MDApp):
    toolBarTitle = "MavLink"
    connected = False

    colors = {
        "Black-primary": [0,0,0,0.9],
        "Gold-primary": [0.78,0.56,0.05,1],
        "Gold-secondary": [0.78,0.56,0.05,0.5],
        "Jewel-primary": [0.00392, 0.14117, 0.3607]
    }
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
    def get_welcome_text(self):
        return translator.translate('welcome')
    def callback(self,x):
        print(x)
        

if __name__ == '__main__':
    ZequentMavLinkApp().run()