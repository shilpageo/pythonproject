

class student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def printvalue(self):
        print("name:",self.name)
        print("id:", self.id)
    def __str__(self):
        return self.name

f=open("exp","r")
for lines in f:
   data=lines.rstrip("\n").split(",")
   print(data)
   name=data[1]
   id=data[0]
   obj=student(name,id)
   print(obj)
   obj.printvalue()

