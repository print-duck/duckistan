a=[23,2,5,2,213,24,63,52,32,4,6]
'''counter=1
Flag=True
j=len(a)
while Flag:
    if counter>=j:
        Flag=False
    if a[counter] < a[counter-1]:
        temp=a[counter]
        a[counter]=a[counter-1]
        a[counter-1]=temp
    print(a,counter)
    counter+=1
    
print(a)
'''
'''
print(len(a))
Flag=True
while Flag:
    print('.........................................')
    Flag=False
    count=0
    for _ in range(len(a)-1):
        print(a[count],a[count+1])
        if a[count] > a[count+1]:
            temp=a[count]
            a[count]=a[count+1]
            a[count]=temp
            Flag=True
        count+=1
print(a)
'''

flag=True
while flag:
    flag=False
    co=0
    for _ in range(len(a)-1):
        if a[co] > a[co+1]:
            a[co],a[co+1]=a[co+1],a[co]
            flag=True
        co+=1
print(a)





    
