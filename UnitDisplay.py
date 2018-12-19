from pickle import load

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.properties import StringProperty


class unitThumbnail(BoxLayout):
    displayedStat = StringProperty('Pts')
    #todo set fixed dimensions for this thumbnail
    def __init__(self, unit, **kwargs):
        super(unitThumbnail, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.unit = unit
        self.spacing = 2
        self.imagePathPrefix = 'Images\\' + unit.faction.lower() + '\\' + unit.faction + '_'
        self.imagePath =  '_'.join(word for word in unit.name.split()) + '.png'
        self.add_widget(Image(source = self.imagePathPrefix + self.imagePath,
                              #size = (self.width, self.height),
                              allow_stretch = False))
        self.add_widget(Label(text = self.unit.name + '\n' + self.unit[self.displayedStat]
                                     + ' ' + self.displayedStat,
                              text_size = (self.width, None),
                              halign = 'center'))


    def changeDisplayedStat(self, newStat):
        self.displayedStat = newStat


class CoreStatSheet(GridLayout):
    def __init__(self,unit,**kwargs):
        super(CoreStatSheet, self).__init__(**kwargs)
        for stat in unit:
            self.add(Label(text = stat))
            self.add(Label(text = unit[stat]))


class InventoryGrid(GridLayout):
    def __init__(self,  **kwargs):
        super(InventoryGrid,self).__init__(**kwargs)


    def refresh(self, invFac):
        faction = invFac
        invPath = 'Data\MasterUnitLists\\' + faction.lower() + '.p'
        if faction != '':
            with open(invPath, 'rb') as P:
                inventory = load(P)
            self.clear_widgets()
            for unit in inventory:
                self.add_widget(unitThumbnail(unit))


    def toggleUnitDisplay(self, type):
        pass
