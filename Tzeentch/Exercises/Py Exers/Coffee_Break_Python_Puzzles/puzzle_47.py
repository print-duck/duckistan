#############################
## id 390
## Puzzle Elo 1755
## Correctly solved 60 %
#############################

words_list = ["bitcoin",
            "cryptocurrency",
            "wallet"]
crawled_text = '''
Research produced by the University of
Cambridge estimates that in 2017,
there are 2.9 to 5.8 million unique
users using a cryptocurrency wallet,
most of them using bitcoin.
'''

split_text = crawled_text.split()
res1 = True in map(lambda word: word in split_text, words_list)
res2 = any(word in words_list for word in split_text)
print(res1 == res2)
