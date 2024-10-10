"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When user input is not an integer. e.g. User enters a string or float.
2. When will a ZeroDivisionError occur?
    When denominator = 0. i.e. When user enters 0 for "Enter the denominator: "
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, include user-input error-checking.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
