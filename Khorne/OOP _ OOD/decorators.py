##decorator: This is a decorator function, it accepts another function as an argument and "decorates it"
##which means that it modifies it in some way and returns the modified version.
##Inside the decorator function, we are defining another inner function called wrapper.
##This is the actual function that does the modification by wrapping the passed function func.


'''def decorator(func):
  def wrapper():
    print("This is printed before the function is called")
    func()
    print("This is printed after the function is called")
  
  return wrapper

def say_hello():
  print("Hello! The function is executing")


say_hello = decorator(say_hello)


say_hello()'''


#Syntactic Decorator

def decorator(func):
  def wrapper():
    print("This is printed before the function is called")
    func()
    print("This is printed after the function is called")
  
  return wrapper

@decorator
def say_hello():
  print("Hello! The function is executing")

def hi():
     print('HI--------')

hi()
#
#say_hello()

