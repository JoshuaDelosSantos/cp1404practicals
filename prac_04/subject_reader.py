"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_data = get_data()
    display_subject_details(subject_data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_data = []
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
            subject_data.append(parts)
    return subject_data


def display_subject_details(subject_data):
    """Display subject details"""
    for subject_details in subject_data:
        print(f"{subject_details[0]} is taught by {subject_details[1]:12} and has {subject_details[2]:3} students")


main()
