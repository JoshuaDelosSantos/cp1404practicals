import random

LOW_NUMBER = 1
HIGH_NUMBER = 45
NUMBER_OF_LINES = 6

quick_picks = int(input("How many quick picks? "))

for i in range(quick_picks):
    numbers = []
    for j in range(NUMBER_OF_LINES):
        number = random.randint(LOW_NUMBER, HIGH_NUMBER)
        while number in numbers:
            number = random.randint(LOW_NUMBER, HIGH_NUMBER)
        numbers.append(number)
    numbers.sort()
    for number in numbers:
        print(f"{number:2}", end=' ')
    print()
