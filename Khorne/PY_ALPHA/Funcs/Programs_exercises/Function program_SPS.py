import random
#Function based program
#a function that returns an argument from three choices,
#the user enter a data in realtime
#the user and the ai are given 5 chances
#if the argument matches to that of the user, the round is ignored
#if the argument meets the win condition, the user's chances are reduced by 1
#if the argument meets the lose condition, the ai's chances are reduced by 1

print("Play . . .")
c=["stone","paper","scissor"] #the ai’s choices are randomly selected from this list
st="stone"
pa="paper"
ci="scissor"
aw="AI  WINS" #printed when lose conditions are met
pw="PLAYER  WINS" #printed when win conditions are met

def player():
    global turn
    global roll
    global st
    global pa
    global ci
    turn=input("") #Calling input from the user where the player has to type stone/paper/scissor.
    if turn in c:
        roll=(random.choice(c)) #random function was used using the library random
        print(roll)
    else: #an else clause is used to find errors or mistakes in the program
        print("Stopped due to invalid input")
    play()
    player()

def play(): #the win and lose conditions are declared using If and elif statements.
    if turn==roll:
        print("draw")
    elif  turn==st:
        if roll==pa:
            print(aw)
        elif roll==ci:
            print(pw)
        else:
            print("malfuncs")
    elif turn==pa:
        if roll==ci:
            print(aw)
        elif roll==st:
            print(pw)
        else:
            print("malfuncs")
    elif turn==ci:
        if roll==st:
            print(aw)
        elif roll==pa:
            print(pw)
        else:
            print("malfuncs")
    else: #an else clause is used to find errors or mistakes in the conditions of the program in realtime
        print("Check Program")   

player()


    
