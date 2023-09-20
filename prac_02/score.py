"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    """Get score and determine result; generate random integer using random module and determine result """
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

    random_score = random.randint(1, 100)
    random_score_result = determine_result(random_score)
    print(random_score_result)


def determine_result(score):
    """Determine result"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Pass"
    else:
        result = "Bad"

    return result


if __name__ == '__main__':
    main()
