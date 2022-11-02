##Hybrid Inheritance: Hybrid inheritance satisfies more than one form of inheritance ie. It may be consists of all types of inheritance that we have done above. It is not wrong if we say Hybrid Inheritance is the combinations of simple, multiple, multilevel and hierarchical inheritance. This type of inheritance is very helpful if we want to use concepts of inheritance without any limitations according to our requirements.
##
##Flow Diagram of Hybrid Inheritance in Python Programming
##hybrid-inheritance-in-python-programming
##
##Syntax of Hybrid Inheritance:
##
###Syntax_Hybrid_inheritance
##
##class PC: 
##	pass
##	
##class Laptop(PC): 
##	pass
##	
##class Mouse(Laptop): 
##	pass
##	
##class Student3(Mouse, Laptop): 
##	pass
	
# Driver's code 
#obj = Student3()
#Note: There is no sequence in Hybrid inheritance that which class will inherit which particular class. You can use it according to your requirements.








'''class PC:
     def fun1(self):
          print('This is PC class')

class Laptop(PC):
     def fun2(self):
          print('This is Laptop class inheriting PC class')

class Mouse(Laptop):
     def fun3(self):
          print('This is Mouse class inheriting Laptop class')

class Student(Mouse, Laptop):
     def fun4(self):
          print('This is Student class inheriting PC and Laptop')

# Driver’s code
obj = Student()
obj1 = Mouse()
obj.fun4()
obj.fun3()'''






'''class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")

class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")

class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")

# Sports Car can inherits properties of Vehicle and Car
class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print("Inside SportsCar class")

# create object
s_car = SportsCar()

s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()'''


