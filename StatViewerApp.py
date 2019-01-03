from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty, ListProperty
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from pickle import load
import os

from armyHeader import FactionSelector
from UnitDisplay import UnitThumbnail


class Overmind(RelativeLayout):
    inventory = ObjectProperty(None, rebind = True)
    current_faction = StringProperty('')

class StatViewerApp(App):

    def _absolutePath(cls, relPath):
        try:
            basePath = sys._MEIPASS
        except:
            basePath = os.path.abspath(".")
        return os.path.join(basePath, relPath)

    R = _absolutePath('','Data\MasterUnitLists\master_inventory.p')

    with open(R, 'rb') as file:
        ModelsMaster = load(file)

    def build(self):
        return self.root





if __name__ == '__main__':
    StatViewerApp().run()
