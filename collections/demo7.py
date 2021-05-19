#remove 1st no removed
#pop remove with index

lst=[]
elst=[]
olst=[]
for i in range(1,101):
    lst.append(i)
for i in lst:
  if(i%2==0):
    elst.append(i)
  else:
    olst.append(i)
print(lst)
print(elst)
print(olst)
