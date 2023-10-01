"""I tried to show variety, hopefully I did them correctly :D"""

# 1.
OUT_FILE_NAME = "name.txt"
name = input("Name: ")
with open(OUT_FILE_NAME, 'w') as out_file:
    print(name, file=out_file)


# 2.
IN_FILE_NAME = "name.txt"
with open(IN_FILE_NAME, 'r') as in_file:
    for line in in_file:
        print(f"Your name is {line.strip()}!")


# 3.
QUESTION_THREE_FILE = "numbers.txt"
question_three_in_file = open(QUESTION_THREE_FILE, 'r')
first_number = int(question_three_in_file.readline())
second_number = int(question_three_in_file.readline())
question_three_in_file.close()

print(first_number + second_number)


# 4.
with open('numbers.txt', 'r') as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(total)
