"""
Emails
Estimate: 30 minutes
Actual: 24 minutes
"""


def main():
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

    for email in email_to_name:
        print(f"{email_to_name[email].title()} ({email})")


def extract_name(email):
    parts = email.split('@')
    possible_name = parts[0]
    if "." in possible_name:
        name = possible_name.split(".")
        return " ".join(name).title()
    return parts[0].title()


main()
