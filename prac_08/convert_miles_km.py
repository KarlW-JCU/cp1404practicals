"""Miles to Km Conversion App"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.6093


class ConvertMilesKm(App):
    """Miles to Km Conversion App"""
    input_miles = StringProperty()
    output_km = StringProperty()

    def build(self):
        """"""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.input_miles = "0"
        self.output_km = "0.00"
        return self.root

    def handle_convert(self, value):
        """Convert input miles to kilometres."""
        try:
            result = round(float(value) * MILES_TO_KM, 4)
            self.output_km = str(result)
        except ValueError:
            self.output_km = "0.0"

    def handle_increment(self, field, value):
        """Increment field by value."""
        try:
            result = int(field) + value
            self.input_miles = str(result)
        except ValueError:
            result = 0 + value
            self.input_miles = str(result)


ConvertMilesKm().run()
