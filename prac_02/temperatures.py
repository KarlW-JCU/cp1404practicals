"""
Temperature conversion program:
Celsius to Fahrenheit
Fahrenheit to Celsius
"""

MENU = ("C - Convert Celsius to Fahrenheit\n"
        "F - Convert Fahrenheit to Celsius\n"
        "Q - Quit\n")


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


main()
