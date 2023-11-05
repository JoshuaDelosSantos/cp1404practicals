"""
CP1404 Practical
Kivy GUI program to convert miles to kilometres
Joshua Delos Santos
Started 05/11/2023
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKilometresAPP(App):
    """ConvertMilesToKilometresAPP is an app for converting miles to kilometres."""

    def build(self):
        """Build the Kivy app from the kv file"""
        Window.size = (500, 400)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesToKilometresAPP().run()
