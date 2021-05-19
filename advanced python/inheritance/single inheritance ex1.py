class Person:       #parent class/base class/super class
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printdet(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Employee(Person):         #child class/sub class/derived class
    def det(self,dept,salary,exp):
            self.dept=dept
            self.salary=salary
            self.exp=exp
    def print(self):
        print(self.dept)
        print(self.salary)
        print(self.exp)
st=Person()
st.details("anu",23,"female")
st.printdet()
st=Employee()
st.det("sales",25000,2)
st.print()
st.details("arun",24,"male")
st.printdet()
st.det("manager",50000,3)
st.print()

