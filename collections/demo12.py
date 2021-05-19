#element found or not found in a string
#it is a linear searching method
lst=[]
lst.append(10)
lst.append(30)
lst.append(20)
lst.append(60)
lst.append(45)
lst.append(36)
lst.append(15)
print(lst)
flag=0
num1=int(input("enter a no"))
for i in lst:
    if (i==num1):
       flag=1
    else:
       pass
if(flag==1):
    print("found")
else:
    print("not found")


#to reduce the complexity use binary search

