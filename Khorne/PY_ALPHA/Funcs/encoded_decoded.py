alp='abcdefghijklmnopqrstuvwxyz'
for i in input('Enter the code to be decoded: '):
    elif i == ' ':
        print(end=' ')
    elif (alp.index(i)+1)%2!=0:
        print(alp[(alp.index(i)+1)*-1],end='')
    elif (alp.index(i)+1)%2==0:
        print(i,alp[(alp.index(i)+1)*-1],end='',sep='')
