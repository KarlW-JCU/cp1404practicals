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

longest_word = max([len(word) for word in word_to_count.keys()])
for word in sorted(word_to_count):
    print(f"{word:<{longest_word}} : {word_to_count[word]:>2}")
