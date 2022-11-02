nice_handle=open("heh.txt", "x")
#nice_handle.close()

nice_handle=open("heh.txt", "w")
nice_handle.write("Hehe...")
nice_handle.close()

nice_handle=open("heh.txt", "a")
n=1
while n < 5:
    n+=1
    nice_handle.write("\nHeh heeeeeee\n")
nice_handle.write("          eehee  ")
nice_handle.close()

print("What does the fox say?")

nice_handle=open("heh.txt", "r")
bird_brain=nice_handle.read()
print(bird_brain)
