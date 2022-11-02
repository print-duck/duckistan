a=['1',
   '22',
   '333',
   '4444',
   '55555',
   '666666',
   '7777777',
   '88888888',
   '999999999']

b=[]
for i in a:
    if len(i)==9:
        b.append('a')
    elif len(i)==8:
        b.append('b')
    elif len(i)==7:
        b.append('c')
    elif len(i)==6:
        b.append('d')
    elif len(i)==5:
        b.append('e')
    else:
        b.append('f')

print(b)

c=['a' if len(i)==9 else 'b' if len(i)==8 else 'c' if len(i)==7 else 'd' if len(i)==6 else 'e' if len(i)==5 else 'f' for i in a]

print(c)

