import random

LOW_NUMBER = 1
HIGH_NUMBER = 45
NUMBER_OF_LINES = 6

quick_picks = int(input("How many quick picks? "))

for i in range(NUMBER_OF_LINES):
    numbers = []
    for j in range(quick_picks):
        numbers.append(random.randint(LOW_NUMBER, HIGH_NUMBER))
    print(sorted(numbers))

