class person:
    def m1(self,name,age):
        self.name=name
        self.age=age
    def printm1(self):
        print(self.name)
        print(self.salary)
class employee:
    def m2(self,salary,dept):
        self.dept=dept
        self.salary=salary
    def printm2(self):
        print(self.dept)
        print(self.salary)

class subchild(person,employee):
    def m3(self):
       print("subchild class")

obj=subchild()
obj=person()
obj.m3()
obj.m2(25000,"sales")
obj.print(printm2)
obj.m1("anu",23)
obj.print(printm1)