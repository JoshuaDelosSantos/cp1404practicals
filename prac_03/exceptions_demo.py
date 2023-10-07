"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?  >>>When the user inputs anything that is not an integer (letters, symbols)
2. When will a ZeroDivisionError occur?  >>>When the user enters 0 for the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?  >>>Yes, LBYL
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("If you enter 0 the 'ZeroDivisionError' will occur!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
