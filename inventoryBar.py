import kivy
from pickle import load
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import StringProperty
from UnitDisplay import UnitThumbnail

kivy.require('1.10.1')


class unitTypeSelector(GridLayout):
    #todo read current faction selection and pickle import master part list
    def __init__(self, **kwargs):
        super(unitTypeSelector,self).__init__(**kwargs)
        self.cols = 2
        for unitType in self.parent.inventory:
            btn = ToggleButton(text=unitType)
            btn.bind(state=self.parent.toggleUnitDislay(unitType))
            self.add_widget(btn)

        btn = ToggleButton(text='All')
        btn = ToggleButton(text='Unavailable')
        self.add_widget()




