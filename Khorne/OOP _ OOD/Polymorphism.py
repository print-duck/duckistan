##Polymorphism in python defines methods in the child class that have the same name as the methods in the
##parent class.In inheritance, the child class inherits the methods from the parent class.
##Also, it is possible to modify a method in achild class that it has inherited from the parent class.

#ex:

##print(len())
##1.string-length of string
##2.list-number of items.
##3.dictionary-number of keys.


# Polymorphic len() function
'''print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))'''

#over riding

'''class First:
     def prawin(self):
          print('first mark')
class Second(First):
     def prawin(self):
          super().prawin()
          print('second mark')
class Third(Second):
     def prawin(self):
          super().prawin()
          print('third mark')

obj=Third()
obj.prawin()'''

'''str1 = "Python"
str2 = "Programming"
print(str1+" "+str2)'''


'''add1=45
add2=55
print(add1+add2)'''


'''class test:
     def add(self):
          print(45+67)
class testing:
     def add(self):
          print('prawin'+'55')
     
obj=test()
obj.add()'''







'''class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
#    animal.make_sound()'''

