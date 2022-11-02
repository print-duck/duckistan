#PYTHON

#SYNTAX
#Syntax is the basic lines of code that we use to script in python or any other coding language
#the syntax refers to the grammar and basic understanding of the Python Interpreter
#For example the below line of code is a syntax written using the FUNCTION "print()"
#There are many FUNCTIONs in Python that we will see going forward

print("Hello World !! ")
#Print is a FUNCTION that displays output when a data is given inside the Parantheses

print("..........................................................................................")
#VARIABLE

#A variable is a basic container for storing data in Python
#Variables can be written with Alphabets or underscores as starting characters such as Uppercase characters ( A, B, K, D, etc..) , Lowercase characters (a,g,s,t,g,r , etc)
#or underscores " _ "

art = 77
J20 = "dorohedoro"
Ark = "kilo"
_paint = "Green"

#Meanwhile a variable name cannot start with any numbers or speacial case characters
#All below variables return an syntax error

#2huh = 223
#$hojo = "jojo"

print("..........................................................................................")
#DATA TYPES
#there are 5 main data types in Python, they are
#Strings, Numerics, Sequences, Sets, Mapping tables, and Booleans

#STRINGS
#Strings are characters such as Alphanumerics or symbols written inside a Double quotes or Single quotes
a= "art ARK 1806 $%^&"
b= 'gale klue'
#both the above variables a and b are strings since they contain characters that are inside either Double quotes or Single quotes
#Strings are referred to as --- Sequence of characters.
#A sequence is an ordered group of elements
#Any sequence in Python can be indexed.

#Indexing is referred to as identifying the position of an element inside the object
#For example,,,
motorsport= "rallycars"
#the position of "c" in the string rallycars can be identified with the positional number-5
print(motorsport[5])
#the above syntax gives the output "c"
#the number of characters in the word "rallycars" is actually 9, and the character "c" is the 6th letter of the word "rallycars"
#but since in python indexing starts from "0" or Zero'th position, the first character "r" is given the positional number-0
print(motorsport[0])
#the above code gives the output "r"

#Back to strings,... Strings are further divided into single line or multiline strings
#single line strings are written only with one set of quotes, such as
singlelinezz = "kilo watts"
#multi line strings or paragraphs are written inside Three sets of quotes
multilinzz = """ Kilo
watts
per
meter
square """

print(singlelinezz)
print(multilinzz)

print("..........................................................................................")
#Since strings can be written inside single quotes or double quotes
#multiline or paragraph strings can also be written inside single or double quotes
singlequtemulinzzz = ''' no
of lines
in this code shall be
4 '''

print(singlequtemulinzzz)

print("..........................................................................................")
#NUMERICS
#Numerics are Integers, floats, and complex
#Integers are whole numbers such as 1,2,3,5,56,654433242,42,4,2424211, -232, -24252, 0, 2323 ... etc
#floats are decimal values such as 0.343, 23.5142, 223.222,  99.23, 0.233, -34.4232, 0.00 , 000.000 , 00.232... etc
#complex are values that carry imaginary ( j ) inside it such as 223.3 + j343
complefef= 2.2+2j
print(type(complefef))

print("..........................................................................................")
#BOOLEANS
#Booleans are either "True" or "False" ...  note that the first letter is capital
#Booleans are mostly used in cheking conditions and specific functions that analyse the data
booltr = True
boolfls = False
print(booltr , boolfls)

print("..........................................................................................")
#SEQUENCES
#There are Lists and Tuples, they are collections of data  that can be stored inside a variable seperated by a comma
#Lists -------
listaha= [ "arto", "arks", "foo", 1, 2, 777, "$$$$" , "42" ]
#The  above variable --- listaha is a list containg data such as strings and integers, they can also contain many other data types
#anykind of data can be placed inside the a list seperated by a comma inside SQUARE BRACKETS [ ]
#lists are Ordered i.e.. they are indexed.
print(listaha[2]) #this syntax gives the value "foo" as the output
#Lists are Mutable .. mutable is the adjective of the word Mutate.. which means to change..
#Lists are Mutable/Changeable because the data/values in the list can be altered ... they can be removed and added
listaha.append("newvals")  #The "append()" METHOD is used to add a new value to the list
print(listaha)
listaha.pop() #The "pop()" METHOD is used to remove a value from the list
print(listaha)
#there are many METHODs in Python that we will see going foward

#Tuples -----
tuplehe= ( "Helix", "loco", "loci" , 1808, "1898", "#$#" )
#the above variable --- tuplehe is a tuple, that is almost the same thing as a list But,
#they are inside round brackets and also they are immutable
#By immutable, the values in a tuple cannot be altered
#Once a tuple is declared, thier elements cannot be removed or new elements cannot be added

#Ordered/indexed objects such as All sequence type data sets allow duplicate values
duplilsit=[ "ark" , "ark", "seventy seven", 322, "ark" ]
duplituple=( "kilo", "kilo", "kilo", "helix", "gert" ,2222, 343, "etc", "etc" ]

print("..........................................................................................")
#SETS
#A set is similar to list or tuple but the values are randomized i.e., the set is Un-orderd or Non indexed
#A set is 


print("..........................................................................................")
#Indentation:
#Indentation refers to the whitespace or the invisible characters we assign in the beggining of a code
