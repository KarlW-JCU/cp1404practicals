"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    """Kivy App to square a number."""

    def build(self):
        """Build Kivy GUI from kv file."""
        Window.size = (400, 200)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation, output to label."""
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Input Error"


SquareNumberApp().run()
