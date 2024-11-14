"""Greeter App"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class Greeter(App):
    """Greeter App"""

    def build(self):
        """Build Kivy GUI"""
        Window.size = (800, 400)
        self.title = "Greeter"
        self.root = Builder.load_file('greeter.kv')
        return self.root

    def handle_greet(self):
        """Display greeting to user_input."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear all text fields."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


Greeter().run()
