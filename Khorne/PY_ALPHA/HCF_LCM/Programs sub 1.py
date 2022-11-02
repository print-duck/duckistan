
print("Program to calculate HCF, LCM of multiple numbers")
def choice():
    ask_c=input("To find HCF or LCM ? ( h / l ) ")
    if ask_c=="h":
        hcf()
    elif ask_c=="l":
        lcm()
    else:
        print("choice: invalid input or unexpected error, please try again")
        choice()

def computr_hv():
    global hv
    temp_c1=[]
    for i in ask_hv:
        for j in range(1, minv):
            if i%j==0:
                temp_c1.append(j)
    #print(temp_c1) #To see all the multiples
    if len(temp_c1)>1:
        temp_c1.remove(1)
    maxv=max(temp_c1,key=temp_c1.count)
    count_hv=temp_c1.count(maxv)
    if  count_hv == len(ask_hv):
        hv=maxv
    elif count_hv != len(ask_hv):
        hv=1
    else:
        print("HCF computational error")
        
def computr_lv():
    temp_c2=[]
    for i in ask_lv:
        if maxv%i ==0:
            temp_c2.append(maxv)
        elif maxv%i !=0:
            maxv += 1
            
             

def hcf():
    global minv
    global ask_hv
    ask_hv=(input("Enter the numbers to find their HCF: "))
    ask_hv=ask_hv.split(",")
    if "1" in ask_hv:
        print("1 is the Greatest common divisor")
        choice()
    ask_hv=[int(i) for i in ask_hv]
    minv=min(ask_hv)
    computr_hv()
    print(hv, "is their HCF or Greatest common divisor")
    choice()
#LCM WIP
def lcm():
    ask_lv=input("enter a few values to be evaluated: ")
    ask_lv=ask_lv.split(",")
    ask_lv=[int(i) for i in ask_lv]
    ask_lv=set(ask_lv)
    maxv=max(ask_lv)
    

choice()
