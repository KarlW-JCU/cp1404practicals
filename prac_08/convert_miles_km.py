"""Miles to Km Conversion App"""

from kivy.app import App
from kivy.lang import Builder


class ConvertMilesKm(App):
    """Miles to Km Conversion App"""

    def build(self):
        """"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root


ConvertMilesKm().run()
