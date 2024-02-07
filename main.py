import tools.i18n as i18n
import kivy
from kivymd.app import MDApp

translator = i18n.Translator('tools/localization/')
translator.set_locale('de')


class ZequentMavLinkApp(MDApp):
    def build(self):
        #self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Dark"
        pass
    def get_welcome_text(self):
        return translator.translate('welcome')
    def callback(self,x):
        print(x)
        

if __name__ == '__main__':
    ZequentMavLinkApp().run()