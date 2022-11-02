def revinc(g):
    for _ in range(len(g)):
        g1=g.pop()
        g1+=1
        g.insert(0,g1)
        g1=0
    g.reverse()
    
a=[1,2,3,4]
revinc(a)
print(a)
