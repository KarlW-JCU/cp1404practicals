"""
CP1404/CP5632 Practical
State names in a dictionary
"""

code_to_name = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(f"Short-hand states: {list(code_to_name.keys())}")

state_code = input("Enter short-hand state: ").upper()
while state_code != "":
    if state_code in code_to_name:
        print(f"{state_code} is, {code_to_name[state_code]}.")
    else:
        print("Invalid input.")
    state_code = input("Enter short-hand state: ").upper()
