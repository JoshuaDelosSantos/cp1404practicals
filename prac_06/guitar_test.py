"""
prac_06 - guitar_test.py

Estimated time: 30 mins
Actual time: 10 mins
"""

from prac_06.guitar import Guitar


def main():
    """Test code for Guitar class"""
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    my_guitar_age = my_guitar.get_age()
    other_guitar = Guitar("Another guitar", 2014, 5)

    print(my_guitar)

    print(f"{my_guitar.name} get_age() - Expected 101. Got {my_guitar_age}")
    print(f"{other_guitar.name} get_age() - Expected 9. Got {other_guitar.get_age()}")
    print(f"{my_guitar.name} is_vintage() - Expected True. Got {my_guitar.is_vintage()}")
    print(f"{other_guitar.name} is_vintage() - Expected False. Got {other_guitar.is_vintage()}")


main()
