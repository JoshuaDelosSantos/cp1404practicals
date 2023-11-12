"""
CP1404 prac_09
taxi_simulator.py
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Run taxi simulator."""
    print("Let's drive!")
    print(MENU)

    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    current_taxi = None
    bill = 0

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            pass
        else:
            print("Invalid choice!")
        bill += get_bill_to_date(current_taxi)
        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()


def display_taxis(taxis):
    """Display list of Taxi objects."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Choose taxi from taxis and set current taxi."""
    try:
        taxi_choice = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_choice]
        return current_taxi
    except IndexError:
        print("Invalid number!")
    except ValueError:
        print("Must be a number!")


def get_bill_to_date(current_taxi):
    """Get bill to date."""
    try:
        bill = current_taxi.get_fare()
    except AttributeError:
        bill = 0
    return bill


main()
