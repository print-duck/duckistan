#############################
## id 349
## Puzzle Elo 1504
## Correctly solved 58 %
#############################

words = ['cat', 'mouse', 'dog']
for word in words[:]:
    if len(word) > 3:
        words.insert(0, word)
print(words[0])
