"""
prac_07 - project_management.py

Estimated time: 120 mins
Actual time: 118 mins
"""

import datetime
from prac_07.project import Project
from operator import attrgetter

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
        "- (A)dd new project\n- (U)pdate project\n- (Q)uit")
DEFAULT_FILENAME = "projects.txt"
LOW_PRIORITY_NUMBER = 1
HIGH_PRIORITY_NUMBER = 10
COMPLETED_PROJECT_PERCENTAGE = 100


def main():
    """Run a program that load and save a data file and use a list of Project objects."""
    projects = load_projects(DEFAULT_FILENAME)
    print(MENU)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = get_valid_filename()
            new_projects = load_projects(filename)
            for project in new_projects:
                projects.append(project)
        elif choice == "S":
            out_filename = get_valid_filename()
            save_projects(projects, out_filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_date_string = get_valid_date_string()
            display_filtered_projects_by_date(projects, filter_date_string)
        elif choice == "A":
            name, start_date, priority, cost_estimate, completion_percentage = get_valid_project_details()
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ").upper()
    save_projects(projects, DEFAULT_FILENAME)
    print("Finished.")


def get_valid_filename():
    """Get a valid filename with the right file extension."""
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
    projects = []
    try:
        with open(filename, 'r', encoding="utf-8-sig") as in_file:
            in_file.readline()  # Ignore header
            for line in in_file:
                parts = line.strip().split('\t')
                name = parts[0]
                start_date = parts[1]
                priority = int(parts[2])
                cost_estimate = float(parts[3])
                completion_percentage = float(parts[4])
                projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))

            print(f"{len(projects)} projects loaded.")

    except ValueError:
        print("Make sure data in the file matches the format!\n"
              "e.g. Name	Start Date	Priority	Cost Estimate	Completion Percentage")

    except FileNotFoundError:
        print("File not found!")

    return projects


def save_projects(projects, filename):
    """Save projects into file."""
    with open(filename, 'w', encoding="utf-8-sig") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                  f"{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display projects."""
    incomplete_projects = []
    completed_projects = []

    projects.sort(key=attrgetter('priority'))

    for project in projects:
        if project.is_complete():
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)

    print("Incomplete projects:")
    for incomplete_project in incomplete_projects:
        # Convert start_date date object to string for output requirement
        incomplete_project.start_date = incomplete_project.start_date.strftime('%d/%m/%Y')
        print(f"\t{incomplete_project}")
        # Revert start_date string to date object
        incomplete_project.start_date = datetime.datetime.strptime(incomplete_project.start_date, '%d/%m/%Y').date()

    print("Completed projects:")
    for completed_project in completed_projects:
        completed_project.start_date = completed_project.start_date.strftime('%d/%m/%Y')
        print(f"\t{completed_project}")
        completed_project.start_date = datetime.datetime.strptime(completed_project.start_date, '%d/%m/%Y').date()


def get_valid_date_string():
    """Get a valid date string in the 'dd/mm/yyyy' format."""
    is_valid_date_string = False
    while not is_valid_date_string:
        date_string = input("Enter a date (dd/mm/yyyy): ")
        try:
            date = datetime.datetime.strptime(date_string, '%d/%m/%Y').date()
            is_valid_date_string = True
            return date.strftime('%d/%m/%Y')
        except ValueError:
            print("Invalid date format. Please use the 'dd/mm/yyyy' format.")


def display_filtered_projects_by_date(projects, filter_date_string):
    """Filter projects by date."""
    print(f"----Showing projects from {filter_date_string}----")

    filter_date = datetime.datetime.strptime(filter_date_string, '%d/%m/%Y').date()

    for project in sorted(projects, key=attrgetter('start_date')):
        if project.start_date >= filter_date:
            # Convert start_date date object to string for output requirement
            project.start_date = project.start_date.strftime('%d/%m/%Y')
            print(project)
            # Revert start_date string to date object
            project.start_date = datetime.datetime.strptime(project.start_date, '%d/%m/%Y').date()


def get_valid_project_details():
    """Get valid project details."""
    print("Let's add a new project")
    name = input("Name: ")
    while name == "":
        print("Project name can not be empty")
        name = input("Name: ")

    start_date = get_valid_date_string()

    priority = get_valid_priority_number()

    is_valid_cost_estimate = False
    while not is_valid_cost_estimate:
        try:
            cost_estimate = float(input("Cost estimate: $"))
            if cost_estimate < 0:
                print("It must cost you something or must be free (0)")
            else:
                is_valid_cost_estimate = True
        except ValueError:
            print("Must be a number")

    completion_percentage = get_valid_completion_percentage()

    return name, start_date, priority, cost_estimate, completion_percentage  # No problem with warning


def get_valid_priority_number():
    """Get a valid priority number."""
    is_valid_priority = False
    while not is_valid_priority:
        try:
            priority = int(input("Priority (1-10): "))
            if priority > HIGH_PRIORITY_NUMBER or priority < LOW_PRIORITY_NUMBER:
                print("1 (Highest priority) - 10 (Lowest priority")
            else:
                is_valid_priority = True
        except ValueError:
            print("Priority must be a number (1-10)")
    return priority  # No problem with warning


def get_valid_completion_percentage():
    """Get a valid completion percentage."""
    is_valid_completion_percentage = False
    while not is_valid_completion_percentage:
        try:
            completion_percentage = float(input("Percent complete: "))
            if completion_percentage < 0 or completion_percentage > COMPLETED_PROJECT_PERCENTAGE:
                print("Must be 0-100")
            else:
                is_valid_completion_percentage = True
        except ValueError:
            print("Percent must be a number")
    return completion_percentage  # No problem with warning


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
    print(chosen_project)  # No problem with warning

    new_completion_percentage = input('New percentage: ')
    if new_completion_percentage == "":  # User to leave blank to retain existing value
        pass
    elif float(new_completion_percentage) < 0 or float(new_completion_percentage) > COMPLETED_PROJECT_PERCENTAGE:
        print("Number must be (0-100)")
        chosen_project.completion_percentage = get_valid_completion_percentage()
    else:  # For special character input
        print("Number must be (0-100)")
        chosen_project.completion_percentage = get_valid_completion_percentage()

    new_priority = input("New Priority: ")
    if new_priority == "":  # User to leave blank to retain existing value
        pass
    elif int(new_priority) < LOW_PRIORITY_NUMBER or int(new_priority) > HIGH_PRIORITY_NUMBER:
        print("Must be a number (1-10)")
        chosen_project.priority = get_valid_priority_number()
    else:  # For special character input
        print("Must be a number (1-10)")
        chosen_project.priority = get_valid_priority_number()


main()
