from kivy.uix.screenmanager import ScreenManager

class ZequentRootScreenManager(ScreenManager):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_current(self, instance, value):
        if(self.current) is '__main_screen__':
            pass
        return super().on_current(instance, value)

    def build(self):
        pass
        