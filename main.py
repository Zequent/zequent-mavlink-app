import i18n
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

translator = i18n.Translator('localization/')
translator.set_locale('de')


class StartScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1

        welcomeLabel = Label(text=translator.translate('welcome'))
        welcomeLabel.font_size = '50dp'

        connectButton = Button(text=translator.translate('connect'))
        connectButton.font_size = '50dp'

        self.add_widget(welcomeLabel)
        self.add_widget(connectButton)

class ZequentMavLinkApp(App):
    def build(self):
        return StartScreen()


if __name__ == '__main__':
    ZequentMavLinkApp().run()