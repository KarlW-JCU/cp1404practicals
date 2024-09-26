"""
Temperature conversion program
Reads from and Writes to file
"""


def main():
    file_in = open('temps_input.txt', 'r')
    file_out = open('temps_output.txt', 'w')
    for line in file_in:
        print(convert_fahrenheit_to_celsius(float(line)), file=file_out)
        # print(convert_celsius_to_fahrenheit(float(line)), file=file_out)
    file_in.close()
    file_out.close()
    print('Done')


def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


main()
