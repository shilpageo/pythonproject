
class parent:
    def m1(self):
         print("inside parent")

class child(parent):
    def m2(self):
         print("inside child class")

class subchild(child):
    def m3(self):
        print("inside subchild")

obj = subchild()
obj.m3()
obj.m2()
obj.m1()
obj2=child()
obj2.m2()
obj2.m1()