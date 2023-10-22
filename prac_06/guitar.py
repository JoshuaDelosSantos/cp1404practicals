"""
prac_06 - guitar.py

Estimated time: 30 mins
Actual time:
"""


class Guitar:
    current_year = 2023

    def __init__(self, name="", year=0, cost=0):
        """Initialise Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of data for Guitar"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self, current_year):
        """Return age of guitar in current year from year of manufacture"""
        return current_year - self.year
