tmpa="alligator"
tmpb="zeus"
tmpc="ark"
tmpd="Red\nis\nsus"
tmp1=12
tmp2=25
tmp3=97
tmp3=str(tmp3)
tmplist=["squirrel","pine_cone","42","$$","KoBoL"]
tmpdict={"cardigan":"black","jean":"blue","helmet":"red","year":1898}
#tmp variables

print("*****Data Types*****")
print("----strings----")
print("\n")

print("----Assigning string to a variable----")
v1=("potato")
print(v1)
print("\n")

print("----Multiline strings----")
v2 ='''arc loop
jelly
kilo
lima
kite
kent\n\n''' #single quotes

v3="""arc loop
jelly
kilo
lima
kite
kent""" #double quotes
print(v2+v3)
print("\n")

print("----strings as arrays----")
print(tmpa[1]) #retriving a data from a varaible using its index
print("\n")

print("----looping through strings----")
for v4 in tmpc:
    print(v4)
print("\n")

print("----string Length----")
print(len(tmpc))
print("\n")

print("----string check----")
print("eu" in tmpb) #checking with an membership operator
print("ze" not in tmpb) #checking for absence of the specified string in a variable
print("\n")

print("----string slicing----")
print(tmpa[0:2]) #sliced of the first letter using a defined range
print(tmpa[:4]) #slicing only the first 3 letters
print(tmpa[5:]) #slicing the first 6 letters off
print(tmpa[-3:]) #slicing up last three letters using Negative Indexing
print("\n")

print("----string Modifications----")
print(tmpa.upper() + " Uppercase")  
print(tmpa.lower() + " Lowercase")
v5="   " + tmpc + " Concatenation" #forming a sentence with whitespace at front with concatenation
print(v5)
v5=v5.strip()+ ", strip() is used to remove whitespaces"
print(v5)
print(v1.replace("pot","gell")) #replace used to change potato into gelato
print("\n")

print("----string splitting----")
print(v5.split())
print("\n")

print("----More of string methods----")
#----STRING METHODS :: capitalize, casefold, center, count, encode, endswith
##expandtabs, find, format, format_map, index, isalnum, isalpha
##isascii, isdecimal, isdigit, isidentifier, islower, isnumeric
##isprintable, isspace, istitle, isupper, join, !just, islower
##lstrip, maketrans, partition, replace, find, index, just
##rpartition, rsplit, rstrip, split, splitlines, startswith
##swapcase, title, translate, zfill----
print("capitalize " + tmpa.capitalize())
tmpa=tmpa.upper()
print("casefold for ALLIGATOR is " + tmpa.casefold())
print("center " + tmpa.center(30, "&"))
print("count " + str(tmpa.count("L")))
print("encode " + str(tmpa.encode()))
print("endswith " + str(tmpa.endswith("R")))
v6="Kan\tAda\tLad"
print("expandtabs " + v6.expandtabs(5))
print("find no of \"k\" in ark :" + str(tmpc.find("k")))
v7="KanAdaLad {} Keep {} Kontrol"
print("format :" +v7.format("Kant","Kollective")) #in format function the parameters are strings or data and cant be variables
print("index " +str(tmpa.index("A",1,8)))
v9="Jul8E9$"
print("isalnum for Jul8E9$ " +str(v9.isalnum()))
print("isdecimal for 97 " +str(tmp3.isdecimal()))#only for numerics in a string and does not attribute to an integer
print("isdigit for ark " +str(tmp3.isdigit()))
print("isprintable for Jul8E9$ " +str(v9.isprintable()))
print("isspace for Jul8E9$ " +str(v9.isspace()))
v10="Ho, %Ao $Wololo To Mo Wo"
print("istitle for : Ho, %Ao $Wololo To Mo Wo "+ str(v10.istitle()))
print("isupper for ALLIGATOR " +str(tmpa.isupper()))
print("join a list: " + ", ".join(tmplist)) #make sure all elements in the list are string
print("ljust : " +tmpa.ljust(20,"U"))
print("maketrans :mapping table and translate functions")
v11=tmpa.maketrans("LIGT","AUTH","A") #making a mapping table for tmpa to change ALLIGATOR to AAUTHOR
print(tmpa.translate(v11)) #translate tmpa ALLIGATOR to AUTHOR using the mapping table v11 and using the translate function
print("partition method: ")
print(v5.partition("ark")) #partition method used on the string ark
print("rfind last A in ALLIGATOR " + str(tmpa.rfind("A"))) #will return -1 because lowercase "a" is not in the word "ALLIGATOR"
print("rindex last A in ALLIGATOR " + str(tmpa.rindex("A")))
print("rjust : " +tmpc.rjust(20,"S"))
print("rpartition method: ")
print(v5.rpartition("ark")) #Same as partition but chooses the last occurence of the specified data to partition
print("rsplit method: ")
print(tmpa.rsplit("L",1)) #the first parameter denotes the string to be used as delimeter, while the second is the max instances
v12=tmpa + "         "
print("rstrip: " + v12.rstrip()) #reverse strip
print("Split lines method: ")
print(tmpd.splitlines())
print("startswith: "+ str(tmpa.startswith("liga",2,6))) #Second and third parameters are optional denoting start and end indices respectively
print("swapcase: "+ tmpa.swapcase())
print("title " + tmpb.title())
print("zfill: " + tmpc.zfill(20))
print("\n")
print("END OF STRING METHODS....................\n")
