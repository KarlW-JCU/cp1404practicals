"""People program."""

from operator import itemgetter

from prac_06.extras.person import Person

people = []
first_name = input("First Name: ")
while first_name != "":
    last_name = input("Last Name: ")
    age = int(input("Age: "))
    new_person = Person(first_name, last_name, age)
    people.append(new_person)
    print(f"{new_person.first_name} added!\n")
    first_name = input("First Name: ")

people.append(Person("Tom", "Testing", 18))
people.append(Person("Dick", "Tator", 80))
people.append(Person("Harry", "Soap", 45))

print("All your friends:")
print(people)
[print(person) for person in people]
