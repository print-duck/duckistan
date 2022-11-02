#############################
## id 370
## Puzzle Elo 1558
## Correctly solved 89 %
#############################

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
print(f(1))