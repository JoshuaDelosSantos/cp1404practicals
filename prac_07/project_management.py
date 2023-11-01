"""
prac_07 - project_management.py

Estimated time: 120 mins
Actual time: 118 mins
"""

import datetime
from prac_07.project import Project

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
        "- (A)dd new project\n- (U)pdate project\n- (Q)uit")


def main():
    """Run a program that load and save a data file and use a list of Project objects."""
    projects = []  # Initialised to avoid warning in line 30
    print(MENU)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            in_filename = get_valid_filename()
            data = load_projects(in_filename)
            # Nested list with Project objects from load_projects data
            projects = [Project(name, start_date, int(priority), float(cost_estimate), float(completion_percentage))
                        for name, start_date, priority, cost_estimate, completion_percentage in data]
            print(f"{len(projects)} projects loaded.")
        elif choice == "S":
            out_filename = get_valid_filename()
            save_projects(projects, out_filename)
        elif choice == "D":
            projects.sort()  # Sorted by priority
            display_projects(projects)
        elif choice == "F":
            filter_date_string = get_valid_date_string()
            filter_projects_by_date(projects, filter_date_string)
        elif choice == "A":
            name, start_date, priority, cost_estimate, completion_percentage = get_valid_project_details()
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ").upper()
    print("Finished.")


def get_valid_filename():
    is_valid_filename = False
    while not is_valid_filename:
        part = input("Filename (.txt): ")
        if part == "":
            print("Input can not be empty!")
        elif ".txt" not in part:
            print("Must have the right file extension!")
        else:
            is_valid_filename = True

    return part  # No problem with potential undefined variable


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
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
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


def get_valid_date_string():
    """Get a valid date string in the 'dd/mm/yyyy' format."""
    while True:
        date_string = input("Enter a date (dd/mm/yyyy): ")
        try:
            date = datetime.datetime.strptime(date_string, '%d/%m/%Y').date()
            return date.strftime('%d/%m/%Y')
        except ValueError:
            print("Invalid date format. Please use the 'dd/mm/yyyy' format.")


def filter_projects_by_date(projects, filter_date_string):
    """Filter projects by date."""
    filtered_projects = []

    print(f"----Showing projects from {filter_date_string}----")
    filter_date = datetime.datetime.strptime(filter_date_string, '%d/%m/%Y').date()

    for project in projects:
        project_date = datetime.datetime.strptime(project.start_date, '%d/%m/%Y').date()

        if project_date >= filter_date:
            filtered_projects.append(project)

    for project in filtered_projects:
        print(project)


def get_valid_project_details():
    """Get valid project details."""
    print("Let's add a new project")
    name = input("Name: ")
    while name == "":
        print("Project name can not be empty")
        name = input("Name: ")

    start_date = get_valid_date_string()

    is_valid_priority = False
    while not is_valid_priority:
        try:
            priority = int(input("Priority (1-10): "))
            if priority > 10 or priority < 1:
                print("1 (Highest priority) - 10 (Lowest priority")
            else:
                is_valid_priority = True
        except ValueError:
            print("Priority must be an integer (1-10)")

    is_valid_cost_estimate = False
    while not is_valid_cost_estimate:
        try:
            cost_estimate = float(input("Cots estimate: $"))
            if cost_estimate < 0:
                print("It must cost you something or must be free (0)")
            else:
                is_valid_cost_estimate = True
        except ValueError:
            print("Must be a number")

    is_valid_completion_percentage = False
    while not is_valid_completion_percentage:
        try:
            completion_percentage = float(input("Percent complete: "))
            if completion_percentage < 0 or completion_percentage > 100:
                print("Must be 0-100")
            else:
                is_valid_completion_percentage = True
        except ValueError:
            print("Percent must be a number")

    return name, start_date, priority, cost_estimate, completion_percentage  # No problem with warning


def update_project(projects):
    """Update a Project completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    is_valid_project_choice = False
    while not is_valid_project_choice:
        try:
            project_choice = int(input("Project choice: "))
            chosen_project = projects[project_choice]

            if project_choice < 0:
                print("No such thing!")
            else:
                is_valid_project_choice = True
        except IndexError:
            print("That project not in the list yet!")
        except ValueError:
            print("Must be a number!")

    # Leave blank to retain existing values
    try:
        new_completion_percentage = float(input('New percentage: '))
        chosen_project.completion_percentage = new_completion_percentage  # No problem with warning
    except ValueError:
        pass
    try:
        new_priority = int(input("New Priority: "))
        chosen_project.priority = new_priority

    except ValueError:
        pass


main()
