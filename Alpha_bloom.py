##data=int(input('? '))
##
##if data < 0:
##    print(data * -1)
##else:
##    print(data)
#range-- .
##for i in range(1,10):
##    print(i-0.5)
##    print(i)
##a==b   # same value
##a is b   #  same object

a= 10000
a-= 10000
a+= 10000
print(id(a))
b=a
print(id(b))
print(a is b)


