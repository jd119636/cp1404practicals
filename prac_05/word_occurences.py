word_to_count = {}
text = "this is a collection of words of nice words this is a fun thing it is"

words = text.split()
print(words)
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

print(word_to_count)

max_length = max((len(word) for word in words))

for word in sorted(word_to_count):
    print(f"{word:{max_length}}: {word_to_count[word]}")
