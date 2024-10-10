"""Display subject details program."""

FILENAME = "subject_data.txt"


def main():
    """Read data from file and print details formatted like: subject,lecturer,number of students."""
    subject_data = load_data()
    print_details(subject_data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])  # ignore PyCharm's warning
        data.append(parts)
    input_file.close()
    return data


def print_details(data):
    """Print data formatted like: subject,lecturer,number of students."""
    for item in data:
        print(f"{item[0]} is taught by {item[1]:>12} and has {item[2]:3} students.")


main()
