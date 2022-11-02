# An simple closure
def parent(child):
    
        def child():
                print('Closure has been called')
        return child

my_closure=parent('a_string_passer_that_takes_the_palce_of_Child')



print(parent)
del parent
# print(parent) The closure exists even after the parent has been deleted
my_closure()

#///////////////////-/////////////////

# define decorator
def decorator_parent(candy_child):
	# define wrapper
	def wrapper():
		print("wrapper start")
		# calling The CANDY inside the wrapper
		candy_child()
		print("wrapper end")	
	return wrapper

# Fuction to be decorated
def A_candy_function():
	print("Candy")
 
# Calling the purpose to be called inside the decorator
candy_wrapped_by_decorator_actually_a_closure = decorator_parent(A_candy_function)
candy_wrapped_by_decorator_actually_a_closure()