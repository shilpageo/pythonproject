f=open("/home/shilpa/Downloads/customer","r")
dict={}
ls=[]
for lines in f:
    data=lines.rstrip("\n").split(",")
    ls.append(data[4])
print(ls)
for i in ls:
    if(i not in dict):
        dict[i]=1
    else:
        dict[i]+=1
for i in dict:
    print(i,",",dict[i])
