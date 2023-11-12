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
            choose_taxi(taxis)
        elif choice == "d":
            pass
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ").lower()


def display_taxis(taxis):
    """Display list of Taxi objects."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    pass


main()
