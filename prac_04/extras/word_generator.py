"""Random word generator program."""

import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

print("Random Word Generator!\n"
      "Enter a word with 'Wildcards' to generate a new word!\n"
      "Valid Wildcards:\n"
      "[%]Consonants\n"
      "[#]Vowels\n"
      "[*]Random\n")

word_format = input("Enter a word format: ").lower()
word = ""
for character in word_format:
    if character == "%":
        word += random.choice(CONSONANTS)
    elif character == "#":
        word += random.choice(VOWELS)
    elif character == "*":
        if random.random() < 0.5:
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    else:
        word += character

print(word)
