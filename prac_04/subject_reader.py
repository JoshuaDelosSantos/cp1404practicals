"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    # input_file = open(FILENAME)
    # for line in input_file:
    #     print(line)  # See what a line looks like
    #     print(repr(line))  # See what a line really looks like
    #     line = line.strip()  # Remove the \n
    #     parts = line.split(',')  # Separate the data into its parts
    #     print(parts)  # See what the parts look like (notice the integer is a string)
    #     parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
    #     print(parts)  # See if that worked
    #     print("----------")
    # input_file.close()
    with open(FILENAME, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])  # Ignore warning, don't worry it's a controlled file :)
            data.append(parts)
    return data


def display_subject_details(data):
    """Display subject details"""
    for subject_details in data:
        subject, teacher_name, number_of_students = subject_details
        print(f"{subject} is taught by {teacher_name} and has {number_of_students} students")


main()
