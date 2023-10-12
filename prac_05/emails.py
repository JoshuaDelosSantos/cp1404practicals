"""
Emails
Estimate: 30 minutes
Actual: 24 minutes
"""


def main():
    """Create a dictionary of email to name and display the contents"""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        email_to_name[email] = name

        choice = input(f"Is your name {name}? (Y/n) ").upper()
        if choice != "Y" and choice != "":
            new_name = input("Name: ")
            email_to_name[email] = new_name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name.title()} ({email})")


def extract_name(email):
    """Extract name from email address"""
    possible_name = email.split('@')[0]
    parts = possible_name.split('.')
    return " ".join(parts).title()


main()
