#############################
## id 195
## Puzzle Elo 1672
## Correctly solved 67 %
#############################

def qsort1(L):
    if L:
        return qsort1([x for x in L[1:] if x < L[0]]) + L[:1] \
               + qsort1([x for x in L[1:] if x >= L[0]])
    return []

def qsort2(L):
    if L:
        return L[:1] + qsort2([x for x in L[1:] if x < L[0]]) \
               + qsort2([x for x in L[1:] if x >= L[0]])
    return []

print(qsort1([0, 33, 22]))
print(qsort2([0, 33, 22]))