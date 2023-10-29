"""
prac_07 - myguitars.py
"""

import csv

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    parts = load_data_from_file(FILENAME)
    guitars = [Guitar(name, year, cost) for name, year, cost in parts]
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def load_data_from_file(filename):
    with open(filename, 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        # Return a nested list with logical data types
        return [[name, int(year), float(cost)] for name, year, cost in reader]


main()
