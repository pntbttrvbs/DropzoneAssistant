from pickle import load

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ObjectProperty, ListProperty


class UnitThumbnail(ButtonBehavior, BoxLayout):
    displayedStat = StringProperty('Pts')
    unit = ObjectProperty(None)

    def changeDisplayedStat(self, newStat):
        self.displayedStat = newStat

    def on_press(self):
        popup = CoreStatSheetPopup(self)
        popup.open()

#todo - separate this out into a corestat sheet, and a popup class. The popup class will enumerate weapons and special skills - which will each get their own corestat row.
class CoreStatSheetPopup(Popup):
    unit = ObjectProperty(None)
    unit_name = StringProperty('')
    unit_stats = ListProperty([])

    def __init__(self, unit,**kwargs):
        super(CoreStatSheetPopup, self).__init__(**kwargs)
        self.unit = unit.unit
        self.unit_name = self.unit['name']
        self.unit_stats = self.unit.statMappings

