def outer(name):
    # this is the enclosing function
    print(name)
    def inner():
        # this is the enclosed function

        # the inner function accessing the outer function's variable 'name'
        print('hello',name)

    return inner

#call the enclosing function by assigning it to a variable
#the enclosing function returns (function_object: inner) to (variable : hello). So that hello=inner
hello=outer('Closure')
#calling the enclosed/nested function by calling the variable with paranthesis, hello() -> inner()
hello()
#But directly calling the nested function, returns an error.
#inner()


#Even after deleting the outer function
#We can access the closure

hello()
print ( outer)
del outer
hello()
#print ( outer)

#dunder to access it's contents
print(hello.__closure__)
print(hello.__closure__[0].cell_contents)

