import random
print("""
SHIELD
""")
helpp=input("type \"help\" for more information on the game ")
if helpp=="help":
    print("~~~~~~~~~~~~~~~~~~~~ \n SHIELD : Defend yourself from oncoming attacks, \n type (h) or (b) to defend your head or body respectively, \n your goal is to survive as long as you can, \n dont die... \n ~~~~~~~~~~~~~~~~~~~~")
ai=["head" , "body"]
player_health=10
score=0

def tryna():
    trya=input("Try again? ( y / n )")
    if trya == "y":
        player_health=10
        narrato()
    elif trya != "y":
        quit()
    else:
        print("try again request failed")
        
def narrato():
    narrat=input("Pick up the shield (s)! or run (r)!")
    if narrat=="s":
        gameon()
    elif narrat=="r":
        quit()
    else:
        print("Too late... \n KRAKK@!! \n ....YOU DIED....")
    tryna()

def helth():
    if player_health < 1:
        print("YOU DIED")
        print("Your score is " , score)
        tryna()
    if player_health <= 2:
        print("*death is nearing..*")
    elif player_health <= 5:
        print("*organ failure due to blood loss*")
    elif player_health <= 8:
        print("*blood is dripping*")
    elif player_health <=10:
        pass
    else:
        print("health system failed")

def roundd():
    global player_health
    defn=input("DEFEND !!")
    aiplay=random.choice(ai)
    if defn=="h":
        if aiplay=="head":
            print("""
            █▀▀▀▀█
     │█░░││░░█│
     └┐░─┼┼─░┌┘
         └┐░││░┌┘
            └┐░░┌┘
                └──┘""")
        elif aiplay=="body":
            print("""
|_O   O_\\
   ---(-'\\
   |\   / |
  / |  |  \ """)
            player_health -= 1
        else:
            print("ai failed")
    elif defn=="b":
        if aiplay=="head":
            print("""
▀▄▄
    ▀▀█▄             ▄▄█▀
            ▀█▄▄▄█▀▀
             ▄█▀▀▄▄
                               ▀▄▄
                                         ▀ """)
            player_health -= 1
        elif aiplay=="body":
            print("""
            █▀▀▀▀█
     │█░░││░░█│
     └┐░─┼┼─░┌┘
         └┐░││░┌┘
            └┐░░┌┘
                └──┘""")
        else:
            print("ai failed")
    elif defn != "h" or defn != "b":
        print("You dropped the Shield!!")
        print("CHOP!! ... YOU DIED")
        tryna()
    else:
        print("round has failed")

def gameon():
    global score
    roundd()
    helth()
    score += 1
    gameon()

narrato()





