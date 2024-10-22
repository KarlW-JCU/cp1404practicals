"""Quick pick generator program."""

from random import randint

VALID_NUMBERS = tuple(range(1, 46))
NUMBER_OF_NUMBERS = 6

number_of_quick_picks = int(input('How many quick picks? '))
while number_of_quick_picks < 0:
    print('Please enter a positive number.')
    number_of_quick_picks = int(input('How many quick picks? '))

for i in range(number_of_quick_picks):
    quick_pick = []
    while len(quick_pick) < NUMBER_OF_NUMBERS:
        random_number = VALID_NUMBERS[randint(1, len(VALID_NUMBERS)) - 1]
        if random_number not in quick_pick:
            quick_pick.append(random_number)
    print(("{:2} " * NUMBER_OF_NUMBERS).format(*sorted(quick_pick)))
