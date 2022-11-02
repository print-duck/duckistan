from random import shuffle as sf

a=[1,3,5,7,8,1,2,9,3,2,4,1,4,5,4,6,7,6,8,6]
a=set(a)
a=list(a)
sf(a)

op_mats=[]
for i in range(3):
    mats=[None]*3
    op_mats.append(mats)

for i in op_mats:
    for k in range(3):
        i[k]=a.pop()
        
print(op_mats)
