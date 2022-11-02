
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
    global temp_c1
    if 1 in ask_hv:
        hv=1
        return
    minv=min(ask_hv)
    temp_c1=[]
    for i in ask_hv:
        for j in range(1, minv):
            if i%j==0:
                temp_c1.append(j)
    #print(temp_c1) #To see multiples
    computr_hv_sub()

def computr_hv_sub():
    global hv
    maxv=max(temp_c1)
    count_max=temp_c1.count(maxv)
    #print(count_max) #To see max count
    if count_max != len(ask_hv):
        temp_c1.remove(maxv)
        computr_hv_sub()
    elif count_max == len(ask_hv):
        hv = maxv
    else:
        print("Sub Computational error")
            
def hcf():
    global ask_hv
    ask_hv=(input("Enter the numbers to find their HCF: "))
    ask_hv=ask_hv.split(",")
    if "1" in ask_hv:
        print("1 is the Greatest common divisor")
        choice()
    ask_hv=[int(i) for i in ask_hv]
    computr_hv()
    print(hv, "is their HCF or Greatest common divisor")
    choice()
#LCM WIP
def lcm():
    ask_lv=input("enter a few values to be evaluated: ")
    ask_lv=ask_lv.split(",")
    ask_lv=[int(i) for i in ask_lv]
    ask_hv=ask_lv
    ask_hv=set(ask_hv)
    maxv=max(ask_hv)
    

choice()
