class Student:
    def __init__(self,id,name,course,mark):
        self.id=id
        self.name=name
        self.course=course
        self.mark=mark
    def printvalue(self):
        print("name:",self.name)
        print("id:", self.id)
        print("course:", self.course)
        print("mark:", self.mark)

    def __str__(self):
        return self.name
#lst=[]
f=open("exp2","r")
for lines in f:
   data=lines.rstrip("\n").split(",")
   #print(data)
   name=data[1]
   id=data[0]
   course=data[2]
   mark=int(data[3])
   obj=Student(name,id,course,mark)
   if mark>190:
     print(obj)
     obj.printvalue()

