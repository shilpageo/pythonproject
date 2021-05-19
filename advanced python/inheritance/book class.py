class book:
    def setval(self,name,author,pages):
        self.name=name
        self.author=author
        self.pages=pages
        print(self.name,self.author,self.pages)
bk=book()
bk.setval("python","abc",986)
#print(bk)

#two string method
#-----------------

class book:
    def setval(self,name,author,pages):
        self.name=name
        self.author=author
        self.pages=pages
        print(self.name,self.author,self.pages)
    def __str__(self):
        return self.name+self.author+str(self.pages)
bk=book()
bk.setval("python","abc",986)
print(bk)
