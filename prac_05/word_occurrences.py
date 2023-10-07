"""
Word Occurrences
Estimate: 20 minutes
Actual:
"""
word_to_count = {}

text = input("Text: ")
words = text.split(" ")
unique_words = set(words)

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

for unique_word in unique_words:
    print(f"{unique_word} : {word_to_count[unique_word]}")

