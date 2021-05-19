class Person:       #parent class/base class/super class
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printdet(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Student(Person):         #child class/sub class/derived class
    def det(self,rollno,school):
            self.rollno=rollno
            self.school=school
    def print(self):
        print(self.rollno)
        print(self.school)
per=Person()
per.details("anu",23,"male")
per.printdet()
st=Student()
st.det(4,"lt")
st.print()
st.details("arun",24,"male")
st.printdet()

