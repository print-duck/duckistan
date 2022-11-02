#program to make an empty list and fill it with values to a total of 10 and show output
a=[]
print("Enter a set of values to make a list")
while len(a)<=9:
    b=input("enter a value: ")
    a.append(b)
print(a)

#program to create two lists with even and odd numbers
#to predefine only two empty lists
#remove the numbers that are divisible by 3 or 7
#to make a sum of the even list
#to multiply the largest value with the smallest value in the odd list
#to combine both the list
#and to print them using FOR and IN loops

a=[] #Predefined empty lists
c=[]

#to get all the values in a single line from the user
b=input("Enter a series of numbers seperated by commas \",\": ")
a=b.split(",")
for i in a:
    c.append(float(i))
a.clear() #clearing the list a to put into reuse
b=[] #converting the string b into a list
for j in c: #seperating the odd and even numbers into lists
    if j%2==0:
        a.append(j)
    else:
       b.append(j)
for k in a: #removing the values divisible by 3 and 7
    if k%3==0 or k%7==0:
        a.remove(k)
for l in b:
    if l%3==0 or l%7==0:
        b.remove(l)
c=0 #converting the list c into an integer
for i in a: #making a sum of the even list
    c+=i
else: 
    a=0 #converting the list a into an integer
    a=max(b)*min(b) #multiplying the maximum and minimum values of the odd list

b.clear() #clearing list b for reuse
b.append(a)
b.append(c)
for j in b: #to output using FOR IN
    print(j)
#.......................Program Completed.................................


        
