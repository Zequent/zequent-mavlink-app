import os
import sys

PROJECT_DIR = os.path.abspath(os.path.dirname(sys.argv[0]))

class Utils:
    @staticmethod
    def getSettingsFile():
        return os.path.abspath("tools/local/settings.json") 

    @staticmethod
    def getTranslatorFolder():
        return ('tools/localization/')
    
    @staticmethod
    def abs_path(*path):
        return os.path.join(PROJECT_DIR, *path)

    @staticmethod
    def getNavigationDrawerItems(translator, sm):
        from kivymd.uix.navigationdrawer import MDNavigationDrawerItem,MDNavigationDrawerLabel,MDNavigationDrawerDivider
        from functools import partial
        import json
        
        f = open(os.path.abspath('tools/local/navigationdrawer.json'))
        data=json.load(f)
        sm.transition.direction = 'down'
        
        navigationItems = []
        for key in data:
            match key:
                case 'main':
                    currentNavigationLabel = MDNavigationDrawerLabel()
                    currentNavigationLabel.text = translator.translate('coworker_translate')
                    navigationItems.append(currentNavigationLabel)
                    for currTranslateKey in data[key]:
                        currentNavigationItem = MDNavigationDrawerItem()
                        currentNavigationItem.icon = 'menu'
                        currentNavigationItem.text = translator.translate(currTranslateKey) 
                        currentNavigationItem.bind(on_press=partial(sm.push_replacement,currTranslateKey))
                        navigationItems.append(currentNavigationItem)
                    navigationItems.append(MDNavigationDrawerDivider())
                    
        
        return navigationItems