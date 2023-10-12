import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6

quick_picks = int(input("How many quick picks? "))

for i in range(quick_picks):
    numbers = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in numbers:
            number = random.randint(MINIMUM, MAXIMUM)
        numbers.append(number)
    numbers.sort()
    print(" ".join(f"{number:2}" for number in numbers))
