import os

class Globals:
    @staticmethod
    def getSettingsFile():
        return os.path.abspath("tools/settings/settings.json") 