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
    units = ListProperty([])
    sheet_name = StringProperty('')
    headers = ListProperty([])
    values = ListProperty([])

    def on_units(self, instance, value):
        self.headers = []
        h = self.headers
        self.values = []
        values = self.values
        o = value[0]
        if self.sheet_name != o['name']:
            h.append('Name')
        for stat in o.statMappings.keys():
            if stat in o and stat != 'WEAPONS':
                h.append(stat)
        for v in value:
            for s in h:
                if s == 'Name':
                    s = 'name'
                t = v[s]
                if type(t) is list:
                    t = '\n'.join(t)
                values.append(t)


class CoreStatPopup(Popup):

    def __init__(self, unit,**kwargs):
        super(CoreStatPopup, self).__init__(**kwargs)
        self.title = unit['name']
        self.container = c = BoxLayout(
            orientation = 'vertical'
        )
        u = CoreStatSheet(sheet_name = unit['name'], units = [unit])
        c.add_widget(u)
        if 'weapons' in unit:
            c.add_widget(CoreStatSheet(sheet_name = 'Weapons', units = unit['WEAPONS']))

        if 'special' in unit.baseStats:
            x = SheetLabel(text ='Special')
            c.add_widget(x)

            for spec in unit['specialtext']:
                x = SpecLabel(text = spec)
                c.add_widget(x)

        self.add_widget(c)

class SpecLabel(Label):
    pass

class SheetLabel(Label):
    pass