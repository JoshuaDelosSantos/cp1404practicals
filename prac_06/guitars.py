"""
prac_06 - guitars.py

Estimated time: 30 mins
Actual time: 20 mins
"""

from prac_06.guitar import Guitar


def main():
    """Run program that uses Guitar class"""
    guitars = []

    print("My guitars!")
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.")
        name = input("Name: ")

    print(f"\n... snip ...\n")

    longest_name_length = max(len(guitar.name) for guitar in guitars)

    for i, guitar in enumerate(guitars, 1):
        my_guitar = guitar
        vintage_string = "" if my_guitar.is_vintage() else "(vintage)"
        print(f"Guitar {i}: {my_guitar.name:>{longest_name_length}} ({my_guitar.year}), "
              f"worth $ {my_guitar.cost:,.2f} {vintage_string}")


main()
