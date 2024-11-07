"""
Word Occurrences
Estimate: 30 minutes
Actual:   12 minutes
"""

string = input("Text: ")
word_to_count = {}
for word in string.split():
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

max_word_length = max((len(word) for word in word_to_count.keys()))
for word in sorted(word_to_count):
    print(f"{word:<{max_word_length}} : {word_to_count[word]:>2}")
