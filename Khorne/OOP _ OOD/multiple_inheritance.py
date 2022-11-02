#Multiple Inheritance: When child class is derived or inherited from more than one parent class. This is called multiple inheritance. In multiple inheritance, we have two parent classes/base classes and one child class that inherits both parent classes properties.

##Diagram of Multiple Inheritance
##multiple-inheritance-in-python-programming
##
##Syntax of multiple inheritance:

#syntax_of_multiple_inheritance

'''class parent_1:
    pass

class parent_2:
    pass

class child(parent_1,parent_2):
    pass

obj = child()'''

#Example 3: 
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
    
obj_1 = Popularity()
#Object_creation
print(obj_1.brand_name_1+" is an "+obj_1.prod_1+' of '+str(obj_1.prod_1_popularity))
print(obj_1.brand_name_2+" is an "+obj_1.prod_2+' of '+str(obj_1.prod_2_popularity))
print(obj_1.brand_name_3+" is an "+obj_1.prod_3+' of '+str(obj_1.prod_3_popularity))

#Output
#Amazon is an Online Ecommerce Store popularity of 100
#Ebay is an Online Store popularity of 70
#OLX is an Online Buy Sell Store popularity of 60
