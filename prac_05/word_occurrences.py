user_input = input("Text: ")
words = user_input.split()

word_counts = {}

# Count the occurrences of each word
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Find the longest word to format output
max_length = max(len(word) for word in word_counts)

# Sort the dictionary by keys (words)
sorted_word_counts = dict(sorted(word_counts.items()))

# Print the word counts aligned properly
for word, count in sorted_word_counts.items():
    print(f"{word:{max_length}} : {count}")
