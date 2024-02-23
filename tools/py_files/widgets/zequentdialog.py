from kivymd.uix.dialog import MDDialog

class ZequentDialog(MDDialog):
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos_hint = {'center_x':.5,'center_y':.5}
    
    def build(self):
        pass