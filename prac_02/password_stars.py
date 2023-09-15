minimum_password_length = 5


def main():
    """Get password from user and print stars according to the length of password"""
    password = get_password()
    print_star(password)


def print_star(password):
    """Print star according to the length of password"""
    print("*" * len(password))


def get_password():
    """Get a password that is not and empty string"""
    password = input("Enter password: ")
    while len(password) < minimum_password_length:
        print("Password not long enough!")
        password = input("Enter password: ")
    return password


main()
