"""
prac_07 - project_management.py

Estimated time: 120 mins
Actual time: Functionality=90 mins Final=
"""

import datetime
from prac_07.project import Project

MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n"
        "(A)dd new project\n(U)pdate project\n(Q)uit")


def main():
    """Run a program that load and save a data file and use a list of Project objects."""
    projects = []
    print(MENU)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            in_filename = get_valid_string("Filename: ")
            data = load_projects(in_filename)
            projects = [Project(name, start_date, int(priority), float(cost_estimate), float(completion_percentage))
                        for name, start_date, priority, cost_estimate, completion_percentage in data]
        elif choice == "S":
            out_filename = get_valid_string("Filename: ")
            save_projects(projects, out_filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice!")
        choice = input(">>> ").upper()
        print(MENU)


def get_valid_string(prompt):
    string = input(prompt)
    while string == "":
        print("Input can not be empty!")
        string = input(prompt)
    return string


def load_projects(filename):
    """Load projects from file."""
    data = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # Ignore header
        for line in in_file:
            parts = line.strip().split('\t')
            data.append(parts)
    return data


def save_projects(projects, filename):
    """Save projects into file."""
    with open(filename, 'w') as out_file:
        print(f"Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                  f"{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display projects."""
    incomplete_projects = []
    completed_projects = []

    for project in projects:
        if project.is_complete():
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"\t{project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"\t{project}")


def filter_projects_by_date(projects):
    """Filter projects by date."""
    filtered_projects = []

    date_string = input("Show projects that start after date (dd/mm/yy): ")  # e.g., "30/9/2022"
    values = [int(part) for part in date_string.split('/')]
    filter_date = datetime.date(values[2], values[1], values[0])
    print(filter_date)

    for project in projects:
        project_date_string = project.start_date
        project_date_values = [int(part) for part in project_date_string.split('/')]
        project_date = datetime.date(project_date_values[2], project_date_values[1], project_date_values[0])

        if project_date >= filter_date:
            filtered_projects.append(project)

    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    """Add new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cots estimate: $"))
    completion_percentage = float(input("Percent complete: "))

    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    """Update a Project completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = int(input("Project choice: "))
    chosen_project = projects[project_choice]
    print(chosen_project)

    try:
        new_completion_percentage = float(input('New percentage: '))
        chosen_project.completion_percentage = new_completion_percentage

        new_priority = int(input("New Priority: "))
        chosen_project.priority = new_priority

    except ValueError:
        pass


main()
