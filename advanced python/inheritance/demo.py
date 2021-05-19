#person child parent student
#child & parent inherit person
#student class inherit child

class person:
    def m1(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name,self.age,self.gender)
class parent(person):
    def m2(self,job,place,salary):
        self.job=job
        self.place=place
        self.salary=salary
        print(self.job,self.place,self.gender)
class child(person):
    def m3(self,school):
        self.school=school
        print(self.school)
class student(child):
    def m4(self,rollno):
        self.rollno=rollno
        print("inside")

obj =person()
obj.m1("anu",20,"f")
obj=parent()
obj.m2("sales","kakanad",25000)
obj=child()
obj.m3("ghss")
obj=student()
obj.m4(8)
