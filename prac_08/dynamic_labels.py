"""Dynamic Labels App"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    """Dynamic Labels App"""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Tom", "Dick", "Harry"]

    def build(self):
        """Build Kivy GUI."""
        self.title = "Dynamic Labels App"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create label for each name in list of names."""
        for name in self.names:
            self.root.add_widget(Label(text=name))


DynamicLabels().run()
