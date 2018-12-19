from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView

from armyHeader import ArmyNameWidget
from UnitDisplay import InventoryGrid

class statViewer(App):
    faction = StringProperty(None)
    factionSelector = AnchorLayout(anchor_y='top', anchor_x='left')
    factionSpinner = ArmyNameWidget(size_hint = (0.25, 0.2))
    unitDisplay = ScrollView(size_hint = (1, 0.8))
    g = InventoryGrid(cols = 5, spacing = 10, size_hint_y = None, height = 3000)
    g.bind(height = g.setter('height'))

    def build(self):
        self.root = RelativeLayout()

        self.root.add_widget(self.factionSelector)

        self.unitDisplay.add_widget(self.g)

        self.root.add_widget(self.unitDisplay)

        self.factionSpinner.bind(faction = self.on_faction)

        self.factionSelector.add_widget(self.factionSpinner)

        return self.root

    def on_faction(self,instance,value):
        self.g.refresh(value)

if __name__ == '__main__':
    statViewer().run()
