"""
CP1404 prac_08: box_layout_demo.py
Joshua Delos Santos 05/11/2023
"""


from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayoutDemo is a Kivy app for box layouts demo."""

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greet."""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handle clear."""
        print("test")
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = ''


BoxLayoutDemo().run()
