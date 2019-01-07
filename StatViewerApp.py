from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang.builder import Builder
from pickle import load
import os,sys
import kivy.resources

from UnitDisplay import UnitThumbnail

def resourcePath(*args):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS,*args)
    return os.path.join(os.path.abspath("."),*args)


class Overmind(RelativeLayout):
    inventory = ObjectProperty(None, rebind = True)
    current_faction = StringProperty('')

class StatViewer(App):

    def _absolutePath(cls, relPath):
        return resourcePath(relPath)

    R = resourcePath('Data\MasterUnitLists\master_inventory.p')

    with open(R, 'rb') as file:
        ModelsMaster = load(file)

    def build(self):
        return Builder.load_file(os.path.join('Data\statviewer.kv'))


if __name__ == '__main__':
    kivy.resources.resource_add_path(resourcePath())
    StatViewer().run()
