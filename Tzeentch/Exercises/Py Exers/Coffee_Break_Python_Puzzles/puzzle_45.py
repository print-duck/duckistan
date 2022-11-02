#############################
## id 371
## Puzzle Elo 1748
## Correctly solved 44 %
#############################

pairs = [(1, 'one'),
         (2, 'two'),
         (3, 'three'),
         (4, 'four')]

# lexicographical sorting (ascending)
pairs.sort(key=lambda pair: pair[1])
print(pairs[0][1])