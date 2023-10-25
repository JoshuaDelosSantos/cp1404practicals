"""
prac_06 - guitar.py

Estimated time: 30 mins
Actual time: 10 mins
"""

CURRENT_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Initialise Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of data for Guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,}"

    def get_age(self):
        """Return age of guitar in current year from year of manufacture"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is vintage by age """
        return CURRENT_YEAR - self.year >= VINTAGE_AGE
