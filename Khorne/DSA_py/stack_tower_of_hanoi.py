'''
STACK - Tower of Hanoi
There are three stacks a,b and c,
transfer all elements of a to c,
rules : higher value element cannot be pushed on top of lower value element
'''
# Stacks a, b and c
a=[5,4,3,2,1]
b=[]
c=[]

def m(from_tower,to_tower):
    popped_data=from_tower.pop()
    if len(to_tower) == 0:
        to_tower.append(popped_data)
    elif popped_data> to_tower[len(to_tower)-1]:
        print("\nHigher value can't be placed next to lower value")
        from_tower.append(popped_data)
    elif popped_data < to_tower[len(to_tower)-1]:
        to_tower.append(popped_data)
    else:
        print("error in movement")

def play():
    val=input().split(",")
    if len(val)!=2:
        print("input error : please retry")
        play()
    val1=val[0]
    val2=val[1]
    
    if val1 == "a":
        if val2=="b":
            m(a,b)
        elif val2=="c":
            m(a,c)
        else:
            print("Please choose second tower either b or c")
    elif val1== "b":
        if val2=="a":
            m(b,a)
        elif val2=="c":
            m(b,c)
        else:
            print("Please choose second tower either a or c")
    elif val1== "c":
        if val2=="a":
            m(c,a)
        elif val2=="b":
            m(c,b)
        else:
            print("Please choose second tower either a or b")
    else:
        print("Please choose first tower a,b or c")
    print("")
    print(a)
    print(b)
    print(c)
    print("")
    play()

try:
    play()
except IndexError:
    print("Stack is empty")
    play()
    
