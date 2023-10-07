"""
CP1404: Prac2 - score_menu.py
"""

from score import determine_result

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Run the score menu program that gets a valid score and then presents a menu for the users to choose from"""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"{score} is {result}")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def print_stars(score):
    """Print star characters"""
    print("*" * score, end=' ')
    print()


main()
