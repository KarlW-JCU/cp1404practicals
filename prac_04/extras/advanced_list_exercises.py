"""Number details program."""


def main():
    """Display number details from user defined list of numbers."""
    numbers = get_numbers()
    print_number_details(numbers)


def get_numbers():
    """Return list of valid numbers."""
    numbers = []
    while True:
        try:
            number = float(input(f"Number {len(numbers) + 1}: "))
            while number >= 0:
                numbers.append(number)
                number = float(input(f"Number {len(numbers) + 1}: "))
            return numbers
        except ValueError:
            print("Invalid input.")


def print_number_details(numbers):
    """Display details from list of numbers."""
    print(f"The first number is {numbers[0]}\n"
          f"The last number is {numbers[-1]}\n"
          f"The smallest number is {min(numbers)}\n"
          f"The largest number is {max(numbers)}\n"
          f"The average of the numbers is {sum(numbers) / len(numbers)}\n")


main()
