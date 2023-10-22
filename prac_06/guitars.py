"""
prac_06 - guitars.py

Estimated time: 30 mins
Actual time: 20 mins
"""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2023


def main():
    """Run program that uses Guitar class"""
    guitars = []
    print("My guitars!")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    print(f"\n... snip ...\n")

    # guitar_names = [Guitar(name).name for name in guitars]
    longest_name = max(len(guitar.name) for guitar in guitars)

    for i, guitar in enumerate(guitars, 1):
        my_guitar = guitar
        vintage_string = "" if my_guitar.is_vintage(CURRENT_YEAR) else "(vintage)"
        print(f"Guitar {i}: {my_guitar.name:>{longest_name}} ({my_guitar.year}), "
              f"worth $ {my_guitar.cost:,} {vintage_string}")


main()
