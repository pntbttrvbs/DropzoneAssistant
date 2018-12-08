from kivy.uix.spinner import Spinner
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivy.app import App
from kivy.properties import NumericProperty

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
        self.factionLogo = Image(source = None, size_hint = (0.75,1))
        self.add_widget(self.factionLogo)
        self.factionSpinner = Spinner(
            text = 'Faction',
            values = ('UCM', 'Scourge','PHR','Shaltari','Resistance')
        )
        self.factionSpinner.bind(text=self.change_image)
        self.add_widget(self.factionSpinner)
        #self.add_widget()

    def change_image(self,spinner,text):
        #todo link this faction selection to the unit display panel
        imagesource = 'Images/' + text.lower() + '/' + text + '.png'
        self.factionLogo.source = imagesource


class RosterWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RosterWidget, self).__init__(**kwargs)
        self.orientation = 'horizontal'


class PointsWidget(BoxLayout):
    gameSizes = {'Skirmish': 999, 'Clash':1999, 'Battle':3000}
    maxPoints = NumericProperty(0)
    #todo insert logic for updating current points value
    currPoints = NumericProperty(0)
    gamesize = None
    def __init__(self, **kwargs):
        super(PointsWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        #todo fix automatic option for gamesize display
        self.gamesizeSpinner = gamesizeSelector(
            text = 'Set Game Size',
            values = ('Skirmish', 'Clash', 'Battle', 'Automatic')
        )

        self.pointsBar = ProgressBar(max = self.maxPoints, size_hint=(0.25, 0.25))
        self.pointsBar.value = 50
        self.add_widget(self.gamesizeSpinner)
        #TODO get this points bar working
        self.add_widget(self.pointsBar)

    def setGameSize(self,newSize):
        self.maxPoints = self.gameSizes[newSize]

class gamesizeSelector(Spinner):
    def __init__(self, **kwargs):
        super(gamesizeSelector, self).__init__(**kwargs)

    def GamesizeLabel(self, data):
        label = data + ' : ' + str(self.parent.currPoints) + '/' + str(self.parent.maxPoints) + ' points'
        return label

    def _on_dropdown_select(self, instance, data, *largs):
        self.parent.setGameSize(data)
        self.text = self.GamesizeLabel(data)
        self.is_open = False

