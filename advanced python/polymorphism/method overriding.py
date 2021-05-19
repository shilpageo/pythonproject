#same method name,same no of parameters

class parent:
    def properties(self):
        print("10 lacs rs,2 car")

    def marry(self):
        print("with ram")

class child(parent):
    def marry(self):
        print("with arun")
c=child()
c.marry()