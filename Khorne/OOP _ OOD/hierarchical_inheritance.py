#Hierarchical inheritance: When we derive or inherit more than one child class from one(same) parent class. Then this type of inheritance is called hierarchical inheritance.

##Flow Diagram of Hierarchical Inheritance in Python Programming
##hierarchical-inheritance-in-python-programming
##
##Syntax of Hierarchical Inheritance:

#syntax_of_hierarchical_inheritance

'''class A:                  #parent_class
    pass
    
class B(A):               #child_class
    pass

class C(A):               #child_class
    pass

class D(A):               #child_class
    pass

obj_1 = B()       #Object_creation
obj_2 = C()
obj_3 = D()'''
 

#Example 5:
#example
from abc import ABC, abstractmethod 
class Brands(ABC):                      #parent_class
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


#Output
#Amazon is an Online Ecommerce Store
#Ebay is an Online Store
#OLX is an Online Buy Sell Store
