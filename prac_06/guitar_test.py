"""
prac_06 - guitar_test.py

Estimated time: 30 mins
Actual time: 10 mins
"""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2023


def main():
    """Test code for Guitar class"""
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    my_guitar_age = my_guitar.get_age(CURRENT_YEAR)
    another_guitar = Guitar("Another guitar", 2014, 5)

    print(my_guitar)

    print(f"{my_guitar.name} get_age() - Expected 101. Got {my_guitar_age}")
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age(CURRENT_YEAR)}")
    print(f"{my_guitar.name} is_vintage() - Expected True. Got {my_guitar.is_vintage(CURRENT_YEAR)}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage(CURRENT_YEAR)}")



main()
