""" PERMUTATIONS
return possible combinations"""

#using itertools module
from itertools import permutations, combinations



a_list=[6,2,4,4]
#Every data in the list is treated as unique data irrespective of the value
# for n is len(a_list) , the number of permutations is, n! .
permut_handler = permutations(a_list)

'''
permut_handler = permutations(a_list, L)
where L is the permutation limit
'''

for i in permut_handler:
     print(i)






