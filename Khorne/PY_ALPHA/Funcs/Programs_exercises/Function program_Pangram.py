def pang():
    c="qwertyuiopasdfghjklzxcvbnm"
    a=input("Enter a sentence check wether if its a pangram, ")
    a=list(a)
    c=list(c)
    pangs=True
    for i in c:
        if i not in a:
            pangs=False
    if pangs==False:
        print("The sentence is not a pangram")
    elif pangs==True:
        print("The sentence is a pangram")

pang()
