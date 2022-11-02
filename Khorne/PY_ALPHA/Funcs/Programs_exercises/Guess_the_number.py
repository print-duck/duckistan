import random
def range_maker():
    global chosen
    global range_lot
    global range_n
    print("Enter the range of numbers n1 to n2")
    n1=int(input("n1 = "))
    n2=int(input("n2 = "))
    range_n=[n1]
    while n1 < n2:
        n1+=1
        range_n.append(n1)
    chosen=random.choice(range_n)

n_try=0
def drawone():
    global n_try
    n_try+=1
    guesser=int(input("Try to guess the Number: "))
    if guesser == chosen:
        print("The guess was right!")
        print("number of tries," , n_try) 
        return
    elif guesser < chosen:
        print("Try again, The number is too low")
        drawone()
    elif guesser > chosen:
        print("Try again, The number is too high")
        drawone()
    else:
        print("prog err")


range_maker()
drawone()
