text = "hello world hello"

# Count occurrences of each word
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
