#############################
## id 159
## Puzzle Elo 1492
## Correctly solved 33 %
#############################

def bsearch(l, value):
    lo, hi = 0, len(l)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if l[mid] < value:
            lo = mid + 1
        elif value < l[mid]:
            hi = mid - 1
        else:
            return mid
    return -1

    
l = [0, 1, 2, 3, 4, 5, 6]
x = 6
print(bsearch(l,x))
