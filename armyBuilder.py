import kivy
from kivy.uix.behaviors import ButtonBehavior

kivy.require('1.10.1')

from army import army

from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivy.config import Config

Config.read('dropzoneAssistant.ini')
Config.set('kivy','window_icon', 'Images/Dropzone-Commander-logo.jpg')
Config.write()

class armyBuilder(App):


    def build_config(self, config):
        config.setdefaults('Rulesets', {'Rule Version':'V2.4.1 (beta)',
                                        'Unit Master':'Michigan (2018)'})

    def build(self):
        self.newArmy = army()
        self.root = root = RootWidget()
        return root

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        self.add_widget(ArmyHeader())
        #self.add_widget(armyRosterBar())
        #self.add_widget(inventoryBar())

class ArmyHeader(BoxLayout):
    def __init__(self, **kwargs):
        super(ArmyHeader, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint =(1,0.5)
        self.add_widget(ArmyNameWidget())
        self.add_widget(RosterWidget())
        self.add_widget(PointsWidget())

class ArmyNameWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ArmyNameWidget, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        #self.add_widget(Image(source = 'Images/ucmlogo.jpg'))
        self.add_widget(Spinner(
            text = 'Faction',
            values = ('UCM', 'Scourge','PHR','Shaltari','Resistance')
        ))
        #self.add_widget()

class RosterWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RosterWidget, self).__init__(**kwargs)
        self.orientation = 'horizontal'


class PointsWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(PointsWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.gamesizeSpinner = gamesizeSelector(
            text = 'Set Game Size',
            values = ('Skirmish', 'Clash', 'Battle', 'Automatic')
        )

        self.gamesize = 'Clash'
        self.points = 50
        #self.pts = currArmy.points
        self.maxPoints = 999
        #self.maxPoints =
        #self.pointsLabel = Label(text=self.GamesizeLabel(), size_hint=(0.25,0.25))
        self.pointsBar = ProgressBar(max = self.maxPoints, size_hint=(0.25, 0.25))

        #let's think about putting a method into this class to update the value?
        self.add_widget(self.gamesizeSpinner)
        self.add_widget(self.pointsBar)


class gamesizeSelector(Spinner):
    def __init__(self, **kwargs):
        super(gamesizeSelector, self).__init__(**kwargs)

    def GamesizeLabel(self, data):
        label = data + ' : ' + str(self.parent.points) + '/' + str(self.parent.maxPoints) + ' points'
        return label

    def _on_dropdown_select(self, instance, data, *largs):
        self.text = self.GamesizeLabel(data)
        self.is_open = False


if __name__ == '__main__':
    armyBuilder().run()