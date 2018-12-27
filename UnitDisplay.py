from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ObjectProperty, ListProperty


class UnitThumbnail(ButtonBehavior, BoxLayout):
    displayedStat = StringProperty('Pts')
    unit = ObjectProperty(None, rebind = True)

    def changeDisplayedStat(self, newStat):
        self.displayedStat = newStat

    def on_press(self):
        popup = CoreStatPopup(self.unit)
        popup.open()

#todo - separate this out into a corestat sheet, and a popup class. The popup class will enumerate weapons and special skills - which will each get their own corestat row.
class CoreStatSheet(BoxLayout):
    unit = ObjectProperty(None, rebind = True)
    unit_name = StringProperty('')
    unit_stats = ListProperty([])

    def __init__(self, unit,**kwargs):
        super(CoreStatSheet, self).__init__(**kwargs)
        self.unit = unit
        self.unit_name = self.unit['name']
        self.unit_stats = self.unit.statMappings.keys()


class CoreStatPopup(Popup):
    unit_name = StringProperty('')
    parts = ListProperty([])

    def __init__(self, unit,**kwargs):
        super(CoreStatPopup, self).__init__(**kwargs)
        self.unit_name = unit['name']
        self.parts = [unit] + unit['weapons']
        self.container = c = BoxLayout(
            orientation = 'vertical'
        )
        for item in self.parts:
            c.add_widget(CoreStatSheet(item))
        self.add_widget(c)




