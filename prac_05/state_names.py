"""
CP1404/CP5632 Practical
State names in a dictionary
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

max_length = -1
for name in CODE_TO_NAME.values():
    if len(name) > max_length:
        max_length = len(name)
for code, name in CODE_TO_NAME.items():
    print(f"{code:<3} is {name:<{max_length}}")

state_code = input("Enter short-hand state: ").upper()
while state_code != "":
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}.")
    except KeyError:
        print("Invalid input.")
    state_code = input("Enter short-hand state: ").upper()
