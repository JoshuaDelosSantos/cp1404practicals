"""
Word Occurrences
Estimate: 20 minutes
Actual: 31 minutes :(
"""
word_to_count = {}

text = input("Text: ")
words = text.split(" ")
longest_word = max(len(word) for word in words)

for word in words:
    # Add the count of the occurrences of the word
    word_to_count[word] = word_to_count.get(word, 0) + 1

for word, count in sorted(word_to_count.items()):
    print(f"{word:{longest_word}} : {count}")
