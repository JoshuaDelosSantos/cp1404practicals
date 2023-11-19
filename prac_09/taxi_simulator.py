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
            drive_taxi(current_taxi)
            bill += get_taxi_bill(current_taxi)
        else:
            print("Invalid choice!")

        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display list of Taxi objects."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Choose taxi from taxis and set current taxi."""
    try:
        taxi_choice = int(input("Choose taxi: "))
        return taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")
    except ValueError:
        print("Must be a number!")


def get_taxi_bill(current_taxi):
    """Get bill to date."""
    try:
        bill = current_taxi.get_fare()
    except AttributeError:
        bill = 0
    return bill


def drive_taxi(current_taxi):
    """Drive current taxi."""
    if not current_taxi:
        print("You need to choose a taxi before you can drive")
    else:
        distance = int(input("Drive how far? "))
        current_taxi.drive(distance)
        current_bill = get_taxi_bill(current_taxi)
        print(f"Your {current_taxi.name} trip cost you ${current_bill:.2f}")


main()
