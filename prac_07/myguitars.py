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

    # From prac_06
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.")
        name = input("Name: ")

    save_guitars_to_file(FILENAME, guitars)


def load_data_from_file(filename):
    with open(filename, 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        # Return a nested list with logical data types
        return [[name, int(year), float(cost)] for name, year, cost in reader]


def save_guitars_to_file(filename, guitars):
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.cost},{guitar.year}", file=out_file)


main()
