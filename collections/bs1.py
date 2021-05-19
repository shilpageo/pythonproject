lst=[4,2,3,11,14,15,10,12,13]
lst.sort()
print(lst)
low=0
upp=len(lst)-1
element=int(input("enter element"))
flag=0
while(low<=upp):
    mid=(low+upp)//2

    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flag=1
        break

if(flag>0):
    print("element found")
else:
    print("not found")



