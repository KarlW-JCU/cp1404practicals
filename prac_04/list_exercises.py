"""Number details and username checker program."""

NUMBER_OF_NUMBERS = 5

print(f"Enter {NUMBER_OF_NUMBERS} numbers to begin! :)")
numbers = []
for i in range(1, NUMBER_OF_NUMBERS + 1):
    numbers.append(float(input(f"Number {i}: ")))
print(f"The first number is {numbers[0]}\n"
      f"The last number is {numbers[-1]}\n"
      f"The smallest number is {min(numbers)}\n"
      f"The largest number is {max(numbers)}\n"
      f"The average of the numbers is {sum(numbers) / len(numbers)}\n")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
is_match = False
user = input("Enter username: ")
for username in usernames:
    if username == user:
        is_match = True
if is_match:
    print(f"Access Granted!")
else:
    print(f"Access Denied!")
