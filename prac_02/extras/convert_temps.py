"""
Fahrenheit to Celsius file conversion program
"""


def main():
    file_in = open('temps_input.txt', 'r')
    file_out = open('temps_output.txt', 'w')
    for line in file_in:
        print(convert_fahrenheit_to_celsius(float(line)), file=file_out)
    file_in.close()
    file_out.close()
    print('Done')

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

main()
