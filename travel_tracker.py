from kivy.app import App
from kivy.lang import Builder

from places import Place
from placecollection import PlaceCollection

class TravelTracker(App):
    def build(self):
        self.title = "TravelTracker"
        self.root = Builder.load_file('TravelTracker.kv')
        return self.root


TravelTracker().run()