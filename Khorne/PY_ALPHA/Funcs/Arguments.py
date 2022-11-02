#Arguments >>>>> Positional, Keyword(kwarg), Normal(Explicit), Default, Arbitrary, 
print("katydid") # Normal, Positional, Keywords args
def katydid(x,y,z): #Normal args/Explicit, without assigning values to the formal parameters
    return x-y-z
    

print(katydid(1996,20,0.5)) #unassigned values, Positional arguments
print(katydid(x=42, z=3.16, y=24)) #assigned values, Keyword arguments(kwarg)

print("grasshopper") #Default args
def grasshopper(x=3777,y=2000,z=1000): #Default args, values assigned to the formal parameters
    return x-y-z

print(grasshopper()) #without any values in the actual parameters, Default arguments
print(grasshopper(7360, y=6000)) #giving an unassigned value (Positional arg) and assigned value(kwarg)
#grasshopper(y=6000,7360)
#grasshopper(7360, y=6000, 1000)
#Both the above function calls return a Syntax error, because Positional args cannot come after kwargs.

print("locust") #Arbitrary args (*args)
def locust(*x):
    print(x) #all the values are stored as a Tuple in the variable 'x'
    return x[0]-x[1]-x[2]

print(locust(9999,8888,7777,6666,5555,4444,3333,2222)) #Here the multiple values are assigned to a single formal parameter with a *asterisk prefixed,
#The formal parameter with a * denotes Arbitrary argument, any parameter assigned with a * can take multiple arguments.
#Eventhough multiple arguments are assigned in the function call the output will only return for the statement in function body.
#The function body involves a statement only with the first 3 values of the arbitrary argument.

print("locust_blue") #Positional arbitrary args (*args)
def locust_blue(*x):
    print(x) #all the values are stored as a Tuple in the variable 'x'
    return x[0]-x[1]

print(locust_blue(777,333,222))
    
print("locust_red") #Arbitrary arguments with change of positions, soon to be used for Keyword arbitrary args or **kwargs
def locust_red(**y):
#def locust_red(x,*y,z):
    a=y[0]-y[1]-y[2]
    return a+x
    #c=b+z
    #print(c)

print(locust_red(2000,100,50,10,10000))
