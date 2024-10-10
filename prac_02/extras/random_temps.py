"""
Random temperature generating/recording program
"""

from random import uniform


def main():
    """Get lower and upper limit then generate a number of random values, recorded to file."""
    lower_limit = int(input('Lower limit: '))
    upper_limit = int(input('Upper limit: '))
    number_of_temperatures = int(input("Number of temperatures: "))
    file_out = open('temps_input.txt', 'w')
    for i in range(number_of_temperatures):
        print(uniform(lower_limit, upper_limit), file=file_out)
    file_out.close()


main()
