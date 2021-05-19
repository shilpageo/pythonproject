#prime


lst=[]
flag=0
for i in range(1,101):
    lst.append(i)
for i in lst:
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        print(i,end=" ")
    flag=0


#exponential