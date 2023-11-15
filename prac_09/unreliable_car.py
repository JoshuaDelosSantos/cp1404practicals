"""
CP1404 prac_09
unreliable_car.py
"""
import random

from prac_09.car import Car
from random import randint

RELIABILITY_THRESHOLD = 100


class UnreliableCar(Car):
    """UnreliableCar class that inherits from Car class."""

    def __init__(self, reliability: float, **kwargs):
        """Initialise Unreliable car instance.

        reliability: float between 0 and 100, that represents the percentage chance that the drive method will drive car
        """
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if generated random number is less than reliability."""
        if randint(0, RELIABILITY_THRESHOLD) < self.reliability:
            super().drive(distance)
        else:
            return distance
