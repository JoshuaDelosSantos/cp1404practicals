"""

CP1404 Practical
Kivy GUI program to convert miles to kilometres
Joshua Delos Santos
Started 05/11/2023

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILE_TO_KILOMETRE_RATE = 1.60934


class ConvertMilesToKilometresAPP(App):
    """ConvertMilesToKilometresAPP is an app for converting miles to kilometres."""
    message = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file"""
        Window.size = (500, 400)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Type in the field & press convert"
        return self.root

    def handle_calculate(self):
        """Handle calculation for converting miles to kilometres."""
        try:
            result = float(self.root.ids.input_number.text) * MILE_TO_KILOMETRE_RATE
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = str(0.0)

    def handle_increment(self, increment):
        """Handle calculation for Up"""
        try:
            if self.root.ids.input_number.text == '':
                result = 0.0 + increment
            else:
                result = float(self.root.ids.input_number.text) + increment
            self.root.ids.input_number.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = str(0.0)

    def handle_update(self):
        """Handle changes to the text input by updating the model from the view."""
        self.message = self.root.ids.input_number.text


ConvertMilesToKilometresAPP().run()
