import random
a=0
b=[]
c=0.7929405067768458
def randomm():
    global a
    b.append(random.random())
    a +=1
    randomm()

try:
    randomm()
except RecursionError:
    print(a)

print(len(b))

if c in b:
    print("Psuedo")
elif c not in b:
    print("Psuedo?")

#979
