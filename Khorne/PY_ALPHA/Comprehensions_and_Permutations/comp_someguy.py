'''
Write a program to find the Names of players who finished the race in second position.
(sorted alphabetically)

input:
1. Number of Players(n)
n,n+1. name of player
n,n+1. time_finished by the player
'''

#n = int(input())
#scoresheet = [[input(), float(input())] for _ in range(n)]
#second_highest = sorted(list(set([time_finished for name, time_finished in scoresheet])))[1]
#print('\n'.join([a for a,b in sorted(scoresheet) if b == second_highest]))


scoresheet = [[input(), float(input())] for _ in range(int(input()))]
print('\n'.join([a for a,b in sorted(scoresheet) if b == sorted(list(set([time_finished for name, time_finished in scoresheet])))[1]]))
