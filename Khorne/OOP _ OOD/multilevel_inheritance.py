#Multilevel Inheritance: In multilevel inheritance, we have one parent class and child class that is derived or inherited from that parent class. We have a grand-child class that is derived from the child class. See the below-given flow diagram to understand more clearly.

##The flow of Multilevel Inheritance in Python
##multilevel-inheritance-in-python
##
##Here A is the parent class for class B and class B is acting as the parent class for grand-child class C.
##
##Syntax of multilevel inheritance:

#Syntax_of_multilevel_inheritance

'''class A:
    pass

class B(A):
    pass

class C(B):
    pass

obj = C()'''

#Example 4: 
#example_of_multilevel_inheritance

class Brands:                       #parent_class
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
