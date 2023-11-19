"""
CP1404 prac_09
silver_service_taxi.py
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi class that inherits from Taxi class."""
    flag_fall = 4.50

    def __init__(self, fanciness: float, **kwargs):
        """ Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):
        """Return a string like a Taxi but with flag fall price."""
        return super().__str__() + f" plus flag fall of ${self.flag_fall:.2f}"

    def get_fare(self):
        """Return price for the taxi trip including flag fall price."""
        return super().get_fare() + self.flag_fall
