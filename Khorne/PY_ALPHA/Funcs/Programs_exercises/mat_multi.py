X = [[12,7,3],
      [4 ,5,6],
      [7 ,8,9]]

Y = [[5,8,1,2],
      [6,7,3,0],
      [4,5,9,1]]


op_mats=[]
for i in range(len(X)):
    mats=[None]*len(Y[0])
    for z in mats:
        mats[mats.index(z)]=0
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            mats[j] += X[i][k] * Y[k][j]
    op_mats.append(mats)

print(op_mats)
