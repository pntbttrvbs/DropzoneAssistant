from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ObjectProperty, ListProperty
from unit import unit


class UnitThumbnail(ButtonBehavior, BoxLayout):
    displayedStat = StringProperty('Pts')
    imageSource = StringProperty('')
    unit = ObjectProperty(None, rebind = True)

    def changeDisplayedStat(self, newStat):
        self.displayedStat = newStat

    def on_press(self):
        popup = CoreStatPopup(self.unit)
        popup.open()



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

        #todo nix this 'parts' property and just add unit, weapons, special. models weapons as special is below.
        #todo: make this a recycleview, so scrolling is possible.
        #todo: fix wrap on special text.
        #todo: I can probably make these labels below a simple template...
        if 'special' in unit.baseStats:

            x = (Label(text ='Special',
                        size_hint = (None,None),
                        halign='left'))
            x.bind(texture_size = x.setter('size'))
            c.add_widget(x)

            for spec in unit['specialtext']:
                x = Label(text = spec,
                          size_hint = (None,None))
                x.bind(texture_size = x.setter('size'))
                c.add_widget(x)
        self.add_widget(c)
