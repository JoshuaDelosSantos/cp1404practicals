minimum_password_length = 5


def main():
    password = get_password()
    print_star(password)


def print_star(password):
    print("*" * len(password))


def get_password():
    password = input("Enter password: ")
    while len(password) < minimum_password_length:
        print("Password not long enough!")
        password = input("Enter password: ")
    return password


main()
