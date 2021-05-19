#class : design pattern
#obiect : real worid entity
#reference : name that refers a memory location of an object

class Person:                           #class name start with capital letter
    def print(self):
        print("inside print method")
pe=Person()
pe.print()


class Person:
    def print(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("inside print method",self.name,self.age,self.gender)
pe.person()
pe.print("anu",23,"female")

re=Person()
re.print("amy",24,"male")
