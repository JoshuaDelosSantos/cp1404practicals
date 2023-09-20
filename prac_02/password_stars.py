"""
CP1404: Prac_02 - password_stars.py
"""

MINIMUM_PASSWORD_LENGTH = 5


def main():
    """Get password from user and print stars according to the length of password"""
    password = get_password()
    print_star(password)


def print_star(password):
    """Print star according to the length of password"""
    print("*" * len(password))


def get_password():
    """Get a password that has characters according to the constant"""
    password = input("Enter password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Password not long enough!")
        password = input("Enter password: ")
    return password


main()
