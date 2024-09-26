"""Simple password program"""


MIN_LENGTH = 8

password = input("Password: ")
while len(password) < MIN_LENGTH:
    print(f"Password must be at least {MIN_LENGTH} characters long.")
    password = input("Password: ")
print("Password: ", "*" * len(password), sep='')
