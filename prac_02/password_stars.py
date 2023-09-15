minimum_password_length = 5

password = input("Enter password: ")
while len(password) < minimum_password_length:
    print("Password not long enough!")
    password = input("Enter password: ")

print("*" * len(password))
