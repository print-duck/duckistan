#Data encapsulation--  data hiding + dynamic binding

#dynamic  binding -- assigning values tob parameter at runtime

#This method complusory use __init__


'''class Calc:
     def add(self,a,b):
          return a+b
     def sub(self,a,b):
          return a-b
     def mul(self,a,b):
          return a*b
     def div(self,a,b):
          return a/b
c=Calc()
print(c.add(25,25))
print(c.sub(45,25))
print(c.mul(5,5))
print(c.div(75,25))'''




'''class Calc:
     def __init__(self,a,b):
          self.a=a                                                      #local instance
          self.b=b
     def add(self):
          return self.a+self.b
     def sub(self):
          return self.a-self.b
     def mul(self):
          return self.a*self.b
     def div(self):
          return self.a/self.b
c=Calc(34,5)
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())'''






