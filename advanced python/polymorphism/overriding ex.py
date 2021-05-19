class person:
    def show(self,num1):
        self.num1=num1
        print("inside person method",self.num1)

class child(person):
    def show(self,num2):
        self.num2
        print("inside child method",self.num2)
per=person()
per.show(3)