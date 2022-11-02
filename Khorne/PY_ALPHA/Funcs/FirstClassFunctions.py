#Functions are first class objects
#functions are called first class OBJECTS because they can be passed as parameters,
#placed inside variables and data structures


def new_f():
    return 24
a=new_f()
b=[new_f(), 34, 'lincoln']
print(a,b)
#///////////////////////////////////////////////////////////////////////////
def function_object():
    print("Hello World")

Hello = function_object #Function is being assigned to a variable
Hello() #variable called using paranthesis

hello= function_object()
print(hello)


#///////////////////////////////////////////////////////////////////////////
def squares_and_returns_integer(val):
    val**=2
    return val

def Higher_order_function_that_prints(func): 
    print(func(x))
x=int(input("enter x "))

Higher_order_function_that_prints(squares_and_returns_integer) #function being passed as argument
#/////////////////////////////////////////////////////////////////////////////////////
def high_func(x):
    
    def func_multiplier(y):
        return x*y

    return func_multiplier #returning a function
    
variable_func = high_func(10)
print(variable_func(2))
