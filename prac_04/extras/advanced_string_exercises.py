"""String program."""

strings = []
string = input('Enter a string: ')
while string != '':
    strings.append(string)
    string = input('Enter a string: ')
strings.sort()

duplicates = []
for i, string in enumerate(strings):
    if string == strings[i - 1]:
        if string not in duplicates:
            duplicates.append(string)

if len(duplicates) > 0:
    print(f"Strings repeated: {", ".join(duplicates)}.")
else:
    print("No repeated strings entered.")
