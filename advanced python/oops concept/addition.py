#class Addition:
 #   def setval(self,num1):
#        self.num1=num1

 #   def printval(self,num2):
 #       self.num2 = num2
  #      print(self.num1+num2)

#per=Addition()
#per.setval(25)
#per.printval(100)


class Add():
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
a=Add()
b=int(input("enter"))
c=int(input("enter"))
a.add(b,c)
