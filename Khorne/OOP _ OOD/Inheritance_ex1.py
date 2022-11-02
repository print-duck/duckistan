Inheritance – Types of Inheritance in Python
What is Inheritance in Python: Inheritance in python programming is the concept of deriving a new class from an existing class. Using the concept of inheritance we can inherit the properties of the existing class to our new class. The new derived class is called the child class and the existing class is called the parent class. Hierarchical inheritance in python, Multilevel inheritance in python including Single and Multiple inheritances are the types of inheritance.

Advantages of Inheritance
Code Reusability: It improves code reusability. We don’t need to write the same code again and again. Using inheritance, we can inherit the features of other classes and also add more features to the derived class.
Reduces the Programmers Efforts: Programmers do not need to write the same code and logic. Hence it reduces the efforts of programmers.
Readability: By implementing concepts of inheritance, the program looks more concise and structured. Which makes it easy to read. This way inheritance also improves the readability of code.
The diagram to understand what inheritance actually is?
single inheritance

In the above flow diagram class A (parent class) and class B (child class) is there. Class B (child class) is derived from class A. Class B holds all the properties of class A.

Syntax to implement inheritance:

class parent_class:
    #parent_class members
    pass
    
class child_class(parent_class):
    #child_class members
    pass

obj = child_class()
Example 1:

#Inheritance Example

class A:
    x = "Parent class variable"
        
class B(A):
    pass

c1 = Test()
obj = B()
print(obj.x)
Output:
#Output
Parent class variable
Explanation: Here we can observe that we have created the object of class B. And we do not have any class members in our class B. But we inherited the properties of class A into class B. The class variable in class A is inherited from class B. Hence it is called using the object of class B.

Types of Inheritance in Python Programming
Types of inheritance: There are five types of inheritance in python programming:

1). Single inheritance
2). Multiple inheritances
3). Multilevel inheritance
4). Hierarchical inheritance
5). Hybrid inheritance

(i). Single inheritance: When child class is derived from only one parent class. This is called single inheritance. The example we did above is the best example for single inheritance in python programming.

Flow Diagram of single inheritance in python programming
single inheritance

Syntax of single inheritance:

#syntax_of_single_inheritance

class class1:               #parent_class
    pass

class class2(class1):       #child_class
    pass

obj_name = class2()
Example 2: 

#syntax_of_single_inheritance

class Brands:               #parent_class
    brand_name_1 = "Amazon"
    brand_name_2 = "Ebay"
    brand_name_3 = "OLX"
    
class Products(Brands):       #child_class
    prod_1 = "Online Ecommerce Store"
    prod_2 = "Online Store"
    prod_3 = "Online Buy Sell Store"
    
obj_1 = Products()          #Object_creation
print(obj_1.brand_name_1+" is an "+obj_1.prod_1)
print(obj_1.brand_name_2+" is an "+obj_1.prod_2)
print(obj_1.brand_name_3+" is an "+obj_1.prod_3)
Output:

#Output
#Amazon is an Online Ecommerce Store
#Ebay is an Online Store
#OLX is an Online Buy Sell Store
(ii). Multiple Inheritance: When child class is derived or inherited from more than one parent class. This is called multiple inheritance. In multiple inheritance, we have two parent classes/base classes and one child class that inherits both parent classes properties.

Diagram of Multiple Inheritance
multiple-inheritance-in-python-programming

Syntax of multiple inheritance:

#syntax_of_multiple_inheritance

class parent_1:
    pass

class parent_2:
    pass

class child(parent_1,parent_2):
    pass

obj = child()
Example 3: 

#example_of_multiple_inheritance

class Brands:               #parent_class
    brand_name_1 = "Amazon"
    brand_name_2 = "Ebay"
    brand_name_3 = "OLX"
    
class Products:            #child_class
    prod_1 = "Online Ecommerce Store"
    prod_2 = "Online Store"
    prod_3 = "Online Buy Sell Store"

class Popularity(Brands,Products):
    prod_1_popularity = 100
    prod_2_popularity = 70
    prod_3_popularity = 60
    
obj_1 = Popularity()          #Object_creation
print(obj_1.brand_name_1+" is an "+obj_1.prod_1))
print(obj_1.brand_name_2+" is an "+obj_1.prod_2))
print(obj_1.brand_name_3+" is an "+obj_1.prod_3))
Output

#Output
#Amazon is an Online Ecommerce Store popularity of 100
#Ebay is an Online Store popularity of 70
#OLX is an Online Buy Sell Store popularity of 60
(iii). Multilevel Inheritance: In multilevel inheritance, we have one parent class and child class that is derived or inherited from that parent class. We have a grand-child class that is derived from the child class. See the below-given flow diagram to understand more clearly.

The flow of Multilevel Inheritance in Python
multilevel-inheritance-in-python

Here A is the parent class for class B and class B is acting as the parent class for grand-child class C.

Syntax of multilevel inheritance:

#Syntax_of_multilevel_inheritance

class A:
    pass

class B(A):
    pass

class C(B):
    pass

obj = C()
Example 4: 

#example_of_multilevel_inheritance

class Brands:                      #parent_class
    brand_name_1 = "Amazon"
    brand_name_2 = "Ebay"
    brand_name_3 = "OLX"
    
class Products(Brands):            #child_class
    prod_1 = "Online Ecommerce Store"
    prod_2 = "Online Store"
    prod_3 = "Online Buy Sell Store"

class Popularity(Products):        #grand_child_class
    prod_1_popularity = 100
    prod_2_popularity = 70
    prod_3_popularity = 60
    
    
obj_1 = Popularity()          #Object_creation
print(obj_1.brand_name_1+" is an "+obj_1.prod_1+" popularity of "+str(obj_1.prod_1_popularity))
print(obj_1.brand_name_2+" is an "+obj_1.prod_2+" popularity of "+str(obj_1.prod_2_popularity))
print(obj_1.brand_name_3+" is an "+obj_1.prod_3+" popularity of "+str(obj_1.prod_3_popularity))

#Output
#Amazon is an Online Ecommerce Store popularity of 100
#Ebay is an Online Store popularity of 70
#OLX is an Online Buy Sell Store popularity of 60
4). Hierarchical inheritance: When we derive or inherit more than one child class from one(same) parent class. Then this type of inheritance is called hierarchical inheritance.

Flow Diagram of Hierarchical Inheritance in Python Programming
hierarchical-inheritance-in-python-programming

Syntax of Hierarchical Inheritance:

#syntax_of_hierarchical_inheritance

class A:                  #parent_class
    pass
    
class B(A):               #child_class
    pass

class C(A):               #child_class
    pass

class D(A):               #child_class
    pass

obj_1 = B()       #Object_creation
obj_2 = C()
obj_3 = D()
 

Example 5:

#example

class Brands:                      #parent_class
    brand_name_1 = "Amazon"
    brand_name_2 = "Ebay"
    brand_name_3 = "OLX"
    
class Products(Brands):            #child_class
    prod_1 = "Online Ecommerce Store"
    prod_2 = "Online Store"
    prod_3 = "Online Buy Sell Store"

class Popularity(Brands):        #grand_child_class
    prod_1_popularity = 100
    prod_2_popularity = 70
    prod_3_popularity = 60

class Value(Brands):
    prod_1_value = "Excellent Value"
    prod_2_value = "Better Value"
    prod_3_value = "Good Value"
    
obj_1 = Products()          #Object_creation
obj_2 = Popularity()
obj_3 = Value()
print(obj_1.brand_name_1+" is an "+obj_1.prod_1)
print(obj_1.brand_name_1+" is an "+obj_1.prod_1)
print(obj_1.brand_name_1+" is an "+obj_1.prod_1)
Output:

#Output
#Amazon is an Online Ecommerce Store
#Ebay is an Online Store
#OLX is an Online Buy Sell Store
5). Hybrid Inheritance: Hybrid inheritance satisfies more than one form of inheritance ie. It may be consists of all types of inheritance that we have done above. It is not wrong if we say Hybrid Inheritance is the combinations of simple, multiple, multilevel and hierarchical inheritance. This type of inheritance is very helpful if we want to use concepts of inheritance without any limitations according to our requirements.

Flow Diagram of Hybrid Inheritance in Python Programming
hybrid-inheritance-in-python-programming

Syntax of Hybrid Inheritance:

#Syntax_Hybrid_inheritance

class PC: 
	pass
	
class Laptop(PC): 
	pass
	
class Mouse(Laptop): 
	pass
	
class Student3(Mouse, Laptop): 
	pass
	
# Driver's code 
obj = Student3()
Note: There is no sequence in Hybrid inheritance that which class will inherit which particular class. You can use it according to your requirements.

Example 6: 

#Example_Hybrid_inheritance
class PC:
def fun1(self):
print(“This is PC class”)

class Laptop(PC):
def fun2(self):
print(“This is Laptop class inheriting PC class”)

class Mouse(Laptop):
def fun3(self):
print(“This is Mouse class inheriting Laptop class”)

class Student(Mouse, Laptop):
def fun4(self):
print(“This is Student class inheriting PC and Laptop”)

# Driver’s code
obj = Student()
obj1 = Mouse()
obj.fun4()
obj.fun3()
