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


    def on_faction(self, instance, value):
        self.g.refresh(value)

class StatViewerApp(App):
    with open('Data\MasterUnitLists\master_inventory.p', 'rb') as file:
        ModelsMaster = load(file)

    def build(self):
#        self.factionSpinner.bind(faction = self.on_faction)
        print(self.root.ids)

        return self.root



if __name__ == '__main__':
    StatViewerApp().run()
