class Emp:
    def setval(self,name,dept,salary):
        self.name=name
        self.dept=dept
        self.salary=salary
        print(self.name,self.dept,self.salary)
    def __str__(self):
        return self.name+str(self.salary)
ep=Emp()
ep.setval("dalibor","manager",50000)
print(ep)

