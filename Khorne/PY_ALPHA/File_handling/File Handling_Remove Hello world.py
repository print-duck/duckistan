#File Handling
#Opening a file inside the same directory

artsoft="" #Creating an empty string for the sake of concatenating lines for getting name of text file
jojo=input("File name? ") #getting the name of the file
jojo+=".txt" #adding a .txt as the file format of the corresponding file
jo=open(jojo,'a+') #Creating a handle for the file
for i in jo: #Iterating each line from the text file
    if i.startswith("Hello"): #Creating a simple condition to remove lines that start with the word "hello"
        continue
    artsoft += i #concatenation of the lines
print("......................")
print(artsoft) #printing the concatenated lines

