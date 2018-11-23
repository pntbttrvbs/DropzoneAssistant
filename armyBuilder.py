import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.base import runTouchApp
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
        config.setdefaults('Rulesets', {'Rule Version':'V2.4.1 (beta)', 'Unit Master':'Michigan (2018)'})

    def build(self):
        top = topBar()
        return top


class topBar(BoxLayout):
    def __init__(self, **kwargs):
        super(topBar, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint =(1,0.1)
        #point this depending on faction choice
        self.add_widget(Image(source = 'Images/ucmlogo.jpg'))
        self.add_widget(pointsLayout())
        print(self.children)


class pointsLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(pointsLayout, self).__init__(**kwargs)
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
        print(self.children)


class gamesizeSelector(Spinner):
    def __init__(self, **kwargs):
        super(gamesizeSelector, self).__init__(**kwargs)

    def GamesizeLabel(self, data):
        label = data + ' : ' + str(self.parent.points) + '/' + str(self.parent.maxPoints) + ' points'
        return label

    def _on_dropdown_select(self, instance, data, *largs):
        self.text = self.GamesizeLabel(data)
        self.is_open = False


class battlegroupsSummaryLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(battlegroupsSummaryLayout, self).__init__(**kwargs)
        self.orientation = 'horizontal'


if __name__ == '__main__':
    armyBuilder().run()