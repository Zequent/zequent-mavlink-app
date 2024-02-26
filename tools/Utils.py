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
