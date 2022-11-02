#Set Programs
#create a set by iterating a string of sentence
#only allowed to create a maximum of two sets
#make a frozen set of vowels or random letters
#remove the letters from the frozen set that are intersecting with the primary set
#iterate the elements of the altered primary set to output

#string of sentence
a="Caught in a landslide, no escape from reality. Open your eyes, look up to the skies and see"
b=set(a)
print(b)
a=input("enter random letters to remove: ")
a=frozenset(a) #frozenset
print(a)
#the below block will return a RuntimeError: Set changed size during iteration
#because a new set should have been provided.
##for i in b:
##    if i in a:
##        b.remove(i) 
#So simple difference will solve it
b-=a
for i in b:
    print(i)
#.............................Program Completed.....................
