a=[] 
i = 1 
n=int(input("To search prime numbers between 0 and "))
b=n
n**=2
while i<= n: 
    if i> 1: 
        
        prime = True
    else: 
        prime = False

    j = 2 
    while j < i: 
        if i%j == 0: 
            prime = False
            break
        j += 1  
    if prime: 
        a.append(i)

    i += 1

print(a[b-1])
