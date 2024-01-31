import i18n
import kivy
from kivy.app import App
from kivy.uix.label import Label

translator = i18n.Translator('localization/')
translator.set_locale('de')

#print(translator.translate('welcome'))

class ZequentMavLinkApp(App):
    def build(self):
        welcomeLabel = Label(text=translator.translate('welcome'))
        welcomeLabel.font_size = '50dp'
        return welcomeLabel


if __name__ == '__main__':
    ZequentMavLinkApp().run()