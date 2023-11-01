"""
prac_07 - myguitars.py
"""

import csv

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read guitars from a file and store them in a list of Guitar objects."""
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
    """Load guitars data from CSV file."""
    parts = []
    with open(filename, 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            year = int(row[1])
            cost = float(row[2])
            parts.append([row[0], year, cost])
    return parts


def save_guitars_to_file(filename, guitars):
    """Save guitars to CSV file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
