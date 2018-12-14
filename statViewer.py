from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout

from armyHeader import ArmyNameWidget
from inventoryBar import inventoryBar

class statViewer(App):
    faction = StringProperty()
    factionSelector = AnchorLayout(anchor_y='top', anchor_x='left')
    factionSpinner = ArmyNameWidget(size_hint = (0.25, 0.2))
    unitDisplay = inventoryBar()
    def build(self):
        self.root = RelativeLayout()



        self.root.add_widget(self.factionSelector)
        self.root.add_widget(self.unitDisplay)

        self.factionSpinner.bind(faction = self.on_faction)

        self.factionSelector.add_widget(self.factionSpinner)

        return self.root

    def on_faction(self,instance,value):
        print('The root value changed to: ' + value)
        self.unitDisplay.refresh(value)

if __name__ == '__main__':
    statViewer().run()
