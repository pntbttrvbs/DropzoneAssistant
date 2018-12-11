import kivy

from unit import unit
from kivy.uix.boxlayout import BoxLayout


class unitThumbnail (BoxLayout):
    #should this be a kivy property?
    displayedStat = 'Pts'

    def __init__(self, unit, **kwargs):
        super(self, unitThumbnail).__init__(**kwargs)
        self.unit = unit
        self.imagePath = '\Images\\' + unit.faction.lower() + unit.name.replace(' ', '_')
        #add image
        #add name label
        #add add stat label

    #add method here to change the displayed stat, I can then call this later from a settings toggle.

