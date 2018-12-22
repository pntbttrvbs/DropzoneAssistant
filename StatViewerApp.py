from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView

from armyHeader import FactionSelector
from UnitDisplay import InventoryGrid


class Overmind(RelativeLayout):
    ModelsMaster = ObjectProperty(None, rebind = True)
    current_faction = StringProperty('')


    def on_faction(self, instance, value):
        self.g.refresh(value)

class StatViewerApp(App):

    def build(self):
#        self.factionSpinner.bind(faction = self.on_faction)
        print(self.root.ids)

        return self.root



if __name__ == '__main__':
    StatViewerApp().run()
