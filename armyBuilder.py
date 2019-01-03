import kivy
from kivy.uix.behaviors import ButtonBehavior

kivy.require('1.10.1')

from groupings import army
from UnitDisplay import UnitThumbnail
from pickle import load

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.properties import NumericProperty,ListProperty,StringProperty


from armyHeader import ArmyHeader
from inventoryBar import inventoryBar

Config.read('dropzoneAssistant.ini')
Config.set('kivy','window_icon', 'Images/Dropzone-Commander-logo.jpg')
Config.write()

class armyBuilder(App):

    newArmy = army()
    armyFaction = StringProperty(newArmy.faction)

    def build_config(self, config):
        config.setdefaults('Rulesets', {'Rule Version':'V2.4.1 (beta)',
                                        'Unit Master':'Michigan (2018)'})

    def build(self):
        self.top = RootWidget()
        return self.top

class RootWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(ArmyHeader())
        #self.add_widget(armyRosterBar())
        self.add_widget(inventoryBar())

if __name__ == '__main__':
    armyBuilder().run()
