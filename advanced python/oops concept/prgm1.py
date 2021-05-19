#class Vehicle:
 #   def print(self,name,modelno):
#        self.name=name
 #       self.modelno=modelno
 #       print("vehicle is",self.name,self.modelno)
#pe=Vehicle()
#pe.print("swift","kl03")


class Person:
    def setval(self,name,age):
        self.name=name
        self.age=age
    def printval(self,gender):
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
per=Person()
per.setval("anu",23)
per.printval("female")





