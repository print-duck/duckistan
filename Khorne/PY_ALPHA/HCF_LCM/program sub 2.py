
ask_hv=[32, 40, 48, 56, 64, 72, 80]


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
#use try and error to replace and optimise methods
    #optimisation should be the base priority for now
    #optimisation can be increase with recursion and exception handling
    
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
    print(temp_c1) #To see all the multiples
    maxv=max(temp_c1,key=temp_c1.count)
    count_hv=temp_c1.count(maxv)
    if  count_hv == len(ask_hv):
        hv=maxv
    elif count_hv != len(ask_hv):
        hv=1
    else:
##        print("HCF computational error")

computr_hv()
print(hv)
