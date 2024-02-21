from kivy.uix.boxlayout import BoxLayout
import tools.i18n as i18n

class MainControllerLayout(BoxLayout):
    #Localization
    translator = i18n.Translator('tools/localization/')

    welcomeText = translator.translate('welcome')

    def __init__(self, **kwargs):
        print(self.root)
        super().__init__(**kwargs)
