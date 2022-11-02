#(i). Single inheritance: When child class is derived from only one parent class. This is called single inheritance. The example we did above is the best example for single inheritance in python programming.

##Flow Diagram of single inheritance in python programming
##single inheritance
##
##Syntax of single inheritance:

#syntax_of_single_inheritance

'''class class1:               #parent_class
    pass

class class2(class1):       #child_class
    pass

obj_name = class2()'''
#Example 2: 

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


#Output
#Amazon is an Online Ecommerce Store
#Ebay is an Online Store
#OLX is an Online Buy Sell Store
