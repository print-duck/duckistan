'''ITERABLE :  an object like an array or objects with a Sequence datatype, a set, or the keys of a dictionary '''

iterable=["apache","bmw","chevorlet","duke","enfield"]

##''' ITERATIONS '''

##for i in iterable:
##    print(i)

##''' ITERATOR : An object that uses the iterator - protocol, __iter__() and __next__() '''

##iterator_object = iterable.__iter__()
##iter_values = iterator_object.__next__()
##print(iter_values)

##print(iter_values)

##print(iterator_object.__next__())
##print(next(iterator_object))
##print(iterator_object.__next__())
##print(next(iterator_object))

##''' An iterator object is a,
##given data using <iter>  The data is given in a sequence to the iterator object,
##the Iterator object is Exhaustible
##the elements in the iterator are popped by using <next> starting from the first element '''

##iterator_object = iterable.__iter__()

##try:
##    while True:
##        iter_values = iterator_object.__next__()
##        print(iter_values)

##''' StopIteration is raised when __next__() is used on an empty Iterator object '''

##try:
##    while True:
##        iter_values = iterator_object.__next__()
##        print(iter_values)

##except StopIteration:
##    pass


##''' A Function using return keyword '''

##def my_function():
##    return 2+5
##    return 777
##
##print(my_function())

##''' GENERATORS :  Functions that use, keyword - yield
##    are called Generators '''


##def my_generator():
##    yield "RED"
##    yield "GREEN"
##    yield "YELLOW"
##    yield "BLUE"
##    yield "PURPLE"


##for i in my_generator():
##    print(i)

##'''LAZY EXECUTION'''

##print(my_generator())
##my_generator()

##iterator_object = my_generator().__iter__()

##print(next(my_generator()))
##generator=my_generator()

##print(next(generator))
##print(next(generator))

##print("LOREM IPSUM")
##print("LOREM IPSUM")

##print(generator.__next__())
##print(generator.__next__())


##'''Makng an custom ITERATOR class using iterator protocols'''
##
##class MyNumbers:
##  def __iter__(self):
##    self.a = 1
##    return self
##
##  def __next__(self):
##    if self.a <= 20:
##      x = self.a
##      self.a += 1
##      return x
##    else:
##      raise StopIteration
##
##values=MyNumbers()
##for i in values:
##    print(i)



##'''ITERATOR objects are more efficient compared to loops
##because the dont take much space and dont store every iterated data
##at once, but iterates each data only when asked,
##but taking it to a further step by making it anonymous and not to store any iterated data,
##we can write GENERATOR EXPRESSIONS
##
##Generator Expressions are same as loop comprehensions but uses (round brackets) instead
##of [square brackets]'''
##
##a=[1,2,3,4,5,6,7]
##''' To find the highest value of squares^2 of the above series of numbers '''
##
##for i in (a**2 for x in a):
##    print(i)



##http://www.dabeaz.com/finalgenerator/


