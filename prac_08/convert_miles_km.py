"""Miles to Km Conversion App"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


class ConvertMilesKm(App):
    """Miles to Km Conversion App"""
    input_miles = StringProperty()
    output_km = StringProperty()

    def build(self):
        """"""
        Window.size = (720, 400)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.input_miles = "0"
        self.output_km = "0.00"
        return self.root

    def handle_convert(self, value):
        """"""
        try:
            result = round(float(value) * 1.6093, 4)
            self.output_km = str(result)
        except ValueError:
            pass

    def handle_increment(self, field, value):
        """"""
        try:
            result = int(field) + value
            self.input_miles = str(result)
        except ValueError:
            pass


ConvertMilesKm().run()
