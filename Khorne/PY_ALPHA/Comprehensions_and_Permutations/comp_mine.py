'''
Write a program to find the Names of players who finished the race in second position.
(sorted alphabetically)

input:
1. Number of Players(n)
n,n+1. name of player
n,n+1. time_finished by the player
'''

a=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    a.append([name,score])
a.sort(key = lambda x: x[1])
print(a)
b=[]
nou=1
while nou < len(a):
    if a[nou][1] > a[0][1]:
        if b==[] or a[nou][1] == b[0][1]:
            b.append(a[nou])
        nou += 1
    elif a[nou][1] == a[0][1]:
        nou += 1
        continue
    else:
        nou += 1
        continue
c=[]
for i in b:
    for j in i:
        if type(j)== str:
            c.append(j)
        else:
            continue
c.sort()
for i in c:
    print(i)
