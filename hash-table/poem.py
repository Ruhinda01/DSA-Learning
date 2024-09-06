#!/usr/bin/python3

word_count = {}
with open('poem.txt', 'r') as f:
    content = f.read()
    words = content.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

print(word_count)
