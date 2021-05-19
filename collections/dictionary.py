#DICTIONARY
#----------

#dic={}
#datas are stored as key value pairs
#name:luminar,loc:kakanad,course:python
#here name,loc,course=keys & luminar,kakanad,course=values
#format=key:value
#value is collected by using its corresponding key  {eg.to get luminar we type print(dic["name"])}

#dic={"name":"luminar","loc":"kakkanad","course":"python","marks":250,"data":10.78}
#print(dic)

#PROPERTIES
#----------

#1.supports hetrogenous data
#2.insertion order is preserved
from typing import Dict, Union

dic1={"name":"luminar","loc":"kakkanad","age":25,"mark":30}
#for i in dic1:
#    print(i,":",dic1[i])
#3.support duplicate values||not supports duplicate key
#4.mutable[can update value in dictonary]
dic1["age"]=29
dic1["mark"]=50  #or we can use operator i.e now mark=30 to get 50 we add 20 so dic1["mark"]+=20
print(dic1)

#delete or pop
del dic1["name"]
print(dic1)

print("total" in dic1)  #check the value is present or not

dic1["total"]=150    #update the value total
print(dic1)
