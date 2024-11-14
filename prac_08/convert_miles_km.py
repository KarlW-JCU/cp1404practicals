"""Miles to Km Conversion App"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesKm(App):
    """Miles to Km Conversion App"""

    def build(self):
        """"""
        Window.size = (720, 400)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root


ConvertMilesKm().run()
