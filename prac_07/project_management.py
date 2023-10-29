"""
prac_07 - project_management.py

Estimated time: 90 mins
Actual time:
"""

import datetime
from prac_07.project import Project

MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n"
        "(A)dd new project\n(U)pdate project\n(Q)uit")


def main():
    print(MENU)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_projects()
        elif choice == "S":
            save_projects()
        elif choice == "D":
            display_projects()
        elif choice == "F":
            filter_projects()
        elif choice == "A":
            add_new_project()
        elif choice == "U":
            update_project()
        else:
            print("Invalid choice!")
            choice = input(">>> ").upper()
        print(MENU)


def load_projects():
    filename = input("Enter filename(.txt): ")

    while filename == "":
        print("Filename cannot be blank!")
        filename = input("Enter filename(.txt): ")




def save_projects():
    pass


def display_projects():
    pass


def filter_projects():
    pass


def add_new_project():
    pass


def update_project():
    pass


main()
