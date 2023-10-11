"""
Word Occurrences
Estimate: 20 minutes
Actual: 31 minutes :(
"""
word_to_count = {}

text = input("Text: ")
words = text.split(" ")
unique_words = set(words)
longest_word = max(len(word) for word in words)

for word in words:
    # Add the count of the occurrences of the word
    word_to_count[word] = word_to_count.get(word, 0) + 1

for unique_word in sorted(unique_words):
    print(f"{unique_word:{longest_word}} : {word_to_count[unique_word]}")
