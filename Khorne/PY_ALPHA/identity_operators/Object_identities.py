#Demonstrating object identities

#Creating some objects
a1="333"
b1=45
c1=["afs"]
#Creating some objects with similar data
a2="333"
b2=45
c2=["afs"]

print("string  ",a1, ":" ,id(a1))
print("integer  ",b1, ":" ,id(b1))
print("list  ",c1, ":" ,id(c1))
print("")
print("string  ",a2, ":" ,id(a2))
print("integer  ",b2, ":" ,id(b2))
print("list  ",c2, ":" ,id(c2))
print("\n\n\n")

#Changing the value of a variable
a1="retired"

print("string  ",a1, ":" ,id(a1))
print("integer  ",b1, ":" ,id(b1))
print("list  ",c1, ":" ,id(c1))
print("")
print("string  ",a2, ":" ,id(a2))
print("integer  ",b2, ":" ,id(b2))
print("list  ",c2, ":" ,id(c2))
print("\n\n\n")

#referencing a list to variable
c1=c2

print("string  ",a1, ":" ,id(a1))
print("integer  ",b1, ":" ,id(b1))
print("list  ",c1, ":" ,id(c1))
print("")
print("string  ",a2, ":" ,id(a2))
print("integer  ",b2, ":" ,id(b2))
print("list  ",c2, ":" ,id(c2))
print("\n\n\n")


#ASSIGNMENT CHANGES THE IDENTITY
#assigning a variable to a string and changing the value of the assigned variable
a1="Alpha"
a2="KILO"
a1=a2
a2=a2.lower()

print("string  ",a1, ":" ,id(a1))
print("integer  ",b1, ":" ,id(b1))
print("list  ",c1, ":" ,id(c1))
print("")
print("string  ",a2, ":" ,id(a2))
print("integer  ",b2, ":" ,id(b2))
print("list  ",c2, ":" ,id(c2))
print("\n\n\n")

#assigning a variable to a List and changing the value of the assigned variable
c1=["Alpha"]
c2=["Kilo"]
c1=c2
c2.pop()


print("string  ",a1, ":" ,id(a1))
print("integer  ",b1, ":" ,id(b1))
print("list  ",c1, ":" ,id(c1))
print("")
print("string  ",a2, ":" ,id(a2))
print("integer  ",b2, ":" ,id(b2))
print("list  ",c2, ":" ,id(c2))
print("\n\n\n")

#A few examples
a=1
a+=1
b=2
print(a is b)

a=1000000000
a+=1
b=1000000001
print(a is b)

a=True
a= not a
b=False
print(a is b)

# Because interpreter interning and compiler folding
