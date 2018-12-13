from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.properties import StringProperty


class unitThumbnail (BoxLayout):
    displayedStat = StringProperty('Pts')

    def __init__(self, unit, **kwargs):
        super(unitThumbnail, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.unit = unit
        self.imagePathPrefix = 'Images\\' + unit.faction.lower() + '\\' + 'Scourge_'
        self.imagePath =  '_'.join(word for word in unit.name.split()) + '.png'
        self.add_widget(Image(source = self.imagePathPrefix + self.imagePath))
        self.add_widget(Label(text = self.unit.name))
        self.add_widget(Label(text = self.unit[self.displayedStat] + ' ' + self.displayedStat))

    def changeDisplayedStat(self, newStat):
        self.displayedStat = newStat