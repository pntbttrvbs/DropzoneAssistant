from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty, ListProperty
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from pickle import load

from armyHeader import FactionSelector
from UnitDisplay import UnitThumbnail


class Overmind(RelativeLayout):
    inventory = ObjectProperty(None, rebind = True)
    current_faction = StringProperty('')

class StatViewerApp(App):
    with open('Data\MasterUnitLists\master_inventory.p', 'rb') as file:
        ModelsMaster = load(file)

    def build(self):
        return self.root



if __name__ == '__main__':
    StatViewerApp().run()
