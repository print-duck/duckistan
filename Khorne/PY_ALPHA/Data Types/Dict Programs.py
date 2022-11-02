#Dictionary trainging program
#Predefine a dictionary with two elements {1:777,666:2}
#unpack and make a sum of both keys and values
#create a series of values with multipliers from 10! (factorial of 10)
#multiply each value in the above series by the sum of unpacked dictionary
#assign a key to each value, keys must be strings from the user
#make a sorting mechanism where user can give sort commands
#by keys sorted by both ascending or descending order
#the output must be recieved by.. For in

a={1:777,666:2} #Predefined dictionary
b=list(a.items()) #unpacking a dictionary
a=list(b[0]+b[1])
b=0
for i in a:
    b+=i #sum of keys and values
c=[]
d=11 #create a series of numbers from 10 to 1
while len(c)<=9:
    e=d-1
    c.append(e)
    d=e-1
    c.append(d)
f=[]
for j in c: #multiplying each value of the list by the sum
    a=j*b
    f.append(a)
a=input("Enter 10 names seperated by commas \",\" to be associated to the values: ") #obtaining keys from user
b=a.split(",")
a= {b[i]: f[i] for i in range(len(b))} #creating a dictionary from two lists
#sorting mechanism for the dictionary a
c=list(a.items())
d=input(" ascending (a) or descending (d)? a/d ")
if d=="a":
    c.sort()
else:
    c.sort(reverse=True)
for i in c: #output by for_in
    print(i)
    

