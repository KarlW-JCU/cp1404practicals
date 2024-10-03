"""File reading program."""

# 1.
new_name = input("Name: ")
out_file = open("name.txt", 'w')
print(new_name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", 'r')
old_name = in_file.read().strip()
in_file.close()
print(f"Hi {old_name}!")

# 3.
with open("numbers.txt", 'r') as in_file:
    number_01 = int(in_file.readline().strip())
    number_02 = int(in_file.readline().strip())
print(number_01 + number_02)

# 4.
total = 0
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)
