import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar

class armyBuilder(App):

    def build(self):
        topBar = AnchorLayout(anchor_x='center', anchor_y='top', size_hint=(1, 0.1))
        pointsLayout = AnchorLayout(anchor_x='right', anchor_y='center')
        pts = 500
        # this will reference the points sum of the current army.

        lbl = Label(text=str(pts))
        #        btn = Button(text='Press me', size_hint=(0.25,0.25))

        pb = ProgressBar(max=1000, size_hint=(0.25, 0.25))
        pb.value = pts

        pointsLayout.add_widget(lbl)
        #        topBar.add_widget(btn)
        pointsLayout.add_widget(pb)
        topBar.add_widget(pointsLayout)

        return topBar
