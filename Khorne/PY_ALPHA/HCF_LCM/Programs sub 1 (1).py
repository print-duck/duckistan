
print("Program to calculate HCF, LCM")
def choice():
    ask_c=input("To find HCF or LCM ? ( h / l ) ")
    if ask_c=="h":
        hcf()
    elif ask_c=="l":
        lcm()
    else:
        print("choice: invalid input or unexpected error, please try again")
        choice()

def computr():
    global hv
    temp_c1=[]
    for i in ask_hv:
        for j in range(1, minv):
            if i%j==0:
                temp_c1.append(j)
    temp_c1.remove(1)
    maxv=max(temp_c1,key=temp_c1.count)
    count_hv=temp_c1.count(7)
    if  count_hv == len(ask_hv):
        hv=maxv
    elif count_hv != len(ask_hv):
        hv=1
    else:
        print("HCF computational error")
    

def hcf():
    global minv
    global ask_hv
    ask_hv=(input("Enter the numbers to find their HCF: "))
    ask_hv=ask_hv.split(",")
    ask_hv=[int(i) for i in ask_hv]
    minv=min(ask_hv)
    computr()
    print(hv, "is their HCF or Greatest common divisor")
    choice()

def lcm():
    ask_lv=input("enter a few values to be evaluated: ")
    ask_lv=ask_lv.split(",")
    ask_lv=[int(i) for i in ask_hv]
    ask_lv=set(ask_lv)
    print(ask_lv)

choice()
