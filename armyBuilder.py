import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar

class armyBuilder(App):

    def build(self):
        return topBar()

class topBar(BoxLayout):
    def __init__(self, **kwargs):
        #topBar = AnchorLayout(anchor_x='center', anchor_y='top', size_hint=(1, 0.1))
        #original topBar above, I think by subclassing the boxlayout, I can just insert the desired modules.
        super(topBar, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint =(1,0.1)
        #point this depending on faction choice
        self.add_widget(Image(source = 'Images/ucmlogo.jpg'))
        self.add_widget(pointsLayout())



class pointsLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(pointsLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        pts = 500
        maxPts = 1000
        gameSize = 'CLASH'
        # this will point to the points sum of the current army, as well as the selected game size.
        pointsLabel = Label(text=gameSize + ': ' + str(pts) + '//' + str(maxPts) + ' POINTS', size_hint=(0.25,0.25))
        pointsBar = ProgressBar(max = maxPts, size_hint=(0.25, 0.25))
        pointsBar.value = pts
        #let's think about putting a method into this class to update the value?
        self.add_widget(pointsLabel)
        self.add_widget(pointsBar)



if __name__ == '__main__':
    armyBuilder().run()