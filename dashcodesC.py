#define decorator_function
def decorator(candy):
    # define wrapper
    def wrapper():
        print("wrapper start")
        # calling The CANDY inside the wrapper
        candy()
        print("wrapper end")    
    return wrapper


#Decorating a function with a decorator_function
@decorator
def A_candy_function():
    print("Candy")


#Calling the decorated function
A_candy_function()



