class Student:
    def setval(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def printval(self,dept,rank):
        self.dept=dept
        self.rank=rank
        print(self.name)
        print(self.rollno)
        print(self.dept)
        print(self.rank)
per=Student()
per.setval("anu",23)
per.printval("computerscience",1)