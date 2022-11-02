from time import sleep as sl
#####   OOP:  CLASSes and OBJECTs, EVERY CLASS can have ATTRIBUTES and METHODS
class Home: #1 CREATE A CLASS, with CLASS-Keyword and give it a name
        def __init__(self): #2 Define ATTRIBUTES with __init__ funtion indented inside class.
                self.wages= 0 ##### Any init or function being defined inside a class must have argument SELF
                self.arms=0
        
        def wages(self, wage): #3 Define METHODS with self argument and placeholders for arguments that can be passed
                self.wages += wage #4 You can use ATTRIBUTES of the class inside the METHOD by adding SELF.

class Arms:
        def __init__(self, name, fort, units):
                self.name= name
                self.fort= fort
                self.units= units
                self.wages=0

        def seige(self, losses):
                self.fort -= losses

        def construction(self, constructs):
                self.wages -= 5000*constructs
                self.fort += constructs

        def recruit(self, recruits):
                self.units += recruits

        def defeat(self):
                print('Your Armies have been vanquished')

        def victory(self):
                print('''...
The Invasion has been crushed
''')

        def transfer(self, department, recruits):
                if recruits> self.units:
                        print('Transfer not possible, Not enough units')
                elif self.units > 0:
                        self.units -= recruits
                        department.units += recruits

class Invasion:
        def __init__(self, enemies, days):
                self.enemies=enemies
                self.days=int(days)


        def wave(self,army):
                for i in range(self.days):
                        def charge(army):
                                global temp_1
                                temp_1=army.units
                                army.units -= self.enemies // army.fort
                                if army.units <0:
                                        army.units=0
                        if army.units <= 0:
                                army.defeat()
                                break
                                
                        charge(army)
                        print((temp_1-army.units), 'Men were killed, on day ', i )
                        sl(2)
                if army.units > 0:
                        army.victory()


def management():
        prompt_2=input('''press (1) to create a new army
press (2) to construct forts
press (3) to recruit new units
press (4) to transfer units
press (5) to display stats
press (6) to Return to Stations.
''')
        if prompt_2 == '1':
                input('Name your army')
                management()
        elif prompt_2 == '2':
                no_of_forts=int(input('Enter the number of Forts to build'))
                army_1.construction(no_of_forts)
                management()
        elif prompt_2 == '3':
                management()
        elif prompt_2 == '4':
                management()
        elif prompt_2 == '5':
                print('Soldiers ',army_1.units)
                print('Forts ',army_1.fort)
                print('Treasury ',army_1.wages)
                input('<>')
                management()
        elif prompt_2 == '6':
                main()
        else:
                print('A few moments have passed')


        
def battle():
        wave_1.wave(army_1)
      
def main():
        prompt_1=int(input('''There is a Horde approaching on the Horizon,..
press (1) to manage your army
press (2) to Defend
'''))
        if prompt_1 == 1:
                management()
        elif prompt_1 == 2:
                battle()
        elif prompt_1 !=1 or prompt_1 !=2:
                print('Please choose your actions properly !')
                main()
        else:
                print('main error')
        prompt_2=input('Enemies approaching...')
        for _ in range(3):
                sl(0.5)
                for _ in range(3):
                        sl(0.5)
                        print('.',end='')
                print('')
        main()

        
army_1=Arms('front',2,300000)
wave_1=Invasion(2000,2)
main()
